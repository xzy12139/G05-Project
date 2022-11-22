# 和用户信息有关的蓝图页
from flask import Blueprint

bp = Blueprint("auth", __name__, url_prefix="/auth")


@bp.route("login")
def login():
    pass
