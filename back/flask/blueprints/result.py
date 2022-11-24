# 和结果展示与分析有关的蓝图页
from flask import Blueprint

bp = Blueprint("auth", __name__, url_prefix="/result")


@bp.route("single")
def single():
    pass
