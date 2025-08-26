from flask import Blueprint, jsonify, request
from ...roast import generate_roast
from ...extensions import limiter, cache

bp = Blueprint("api", __name__)

@bp.get("/health")
@cache.cached(timeout=30)
def health():
    return {"status": "ok"}, 200

@bp.post("/roast")
@limiter.limit("20 per minute")
def roast_api():
    data = request.get_json(silent=True) or {}
    name = data.get("name", "")
    return jsonify(generate_roast(name))
