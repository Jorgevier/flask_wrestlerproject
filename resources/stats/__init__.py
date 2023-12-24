from flask_smorest import Blueprint

bp = Blueprint('stats', __name__ , description='Ops on stats', url_prefix='/stat')

from . import routes