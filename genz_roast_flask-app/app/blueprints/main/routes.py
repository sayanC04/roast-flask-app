from flask import Blueprint, render_template, request
from ...roast import generate_roast
from ...extensions import limiter

bp = Blueprint("main", __name__)

@bp.get("/")
@limiter.limit("10 per minute")
def index():
    return render_template("index.html", roast=None)

@bp.post("/")
@limiter.limit("15 per minute")
def roast_name():
    name = request.form.get("name", "")
    result = generate_roast(name)
    return render_template("index.html", roast=result)
