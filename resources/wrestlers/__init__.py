from flask_smorest import Blueprint

bp = Blueprint('wrestlers', __name__ , description='Operations for wrestlers')

from . import routes, auth_routes