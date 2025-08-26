from __future__ import annotations
from flask import Flask
from .config import get_config
from .extensions import limiter, cache

def create_app(env: str | None = None) -> Flask:
    app = Flask(__name__, template_folder="templates", static_folder="static")

    # Configuration
    app.config.from_object(get_config(env or "production"))

    # Init extensions
    limiter.init_app(app)
    cache.init_app(app)

    # Register blueprints
    from .blueprints.main.routes import bp as main_bp
    from .blueprints.api.routes import bp as api_bp
    app.register_blueprint(main_bp)
    app.register_blueprint(api_bp, url_prefix="/api/v1")

    # App-level security headers
    @app.after_request
    def attach_security_headers(response):
        response.headers.setdefault("X-Content-Type-Options", "nosniff")
        response.headers.setdefault("X-Frame-Options", "DENY")
        response.headers.setdefault("Referrer-Policy", "no-referrer")
        csp = app.config.get("CONTENT_SECURITY_POLICY") or "default-src 'self' 'unsafe-inline' https://fonts.googleapis.com https://fonts.gstatic.com;"
        response.headers.setdefault("Content-Security-Policy", csp)
        return response

    # Error handlers
    from flask import render_template, jsonify, request
    @app.errorhandler(404)
    def not_found(e):
        if request.accept_mimetypes.best == "application/json":
            return jsonify({"error": "Not found"}), 404
        return render_template("404.html"), 404

    @app.errorhandler(429)
    def ratelimit(e):
        return jsonify({"error": "Too many requests, chill 😮‍💨"}), 429

    @app.errorhandler(500)
    def server_error(e):
        app.logger.exception("Unhandled server error: %s", e)
        return jsonify({"error": "Something went boom. We’re on it."}), 500

    return app
