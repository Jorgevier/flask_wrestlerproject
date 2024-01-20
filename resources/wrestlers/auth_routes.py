from flask_jwt_extended import create_access_token

from models import WrestlerModel

from . import bp 
from schemas import WrestlerLogin



@bp.post('/login')
@bp.arguments(WrestlerLogin)
def login(wrestler_data):
    wrestler = WrestlerModel.query.filter_by(username = wrestler_data['username']).first()
    if wrestler and wrestler.check_password(wrestler_data['password']):
        access_token = create_access_token(wrestler.id)
        return{'token': access_token}
    return{'message':'Invalid user data'}
