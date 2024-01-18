from flask import request
from uuid import uuid4
from flask.views import MethodView
from flask_smorest import abort

from . import bp
from db import wrestlers

from schemas import WrestlerSchema
from models.wrestler_models import WrestlerModel


@bp.route('/wrestlers/<wrestler_id>')
class Wrestler(MethodView):

    @bp.response(200, WrestlerSchema)
    def get(self, wrestler_id):
        user = UserModel.query.get(wrestler_id)
        if wrestler:
            return wrestler  
        else:
            abort (400, message="that wrestler is not found")


    @bp.arguments(WrestlerSchema)
    def put(self, wrestler_data, wrestler_id):
        wrestler = WrestlerModel.query.get(user_id)
        if wrestler:
            wrestler.from_dict(wrestler_data)
            wrestlers.commit()
            return { 'message': f'{wrestlers.athlete} updated'}, 202
        abort (400, message="invalid user")
        
    def delete(self, wrestler_id):
        wrestler = WrestlerModel.query.get(wrestler_id)
        if wrestler:
            wrestler.delete()
            return { 'message': f'wrestler: {wrestler.athlete} Deleted' }, 202
        return {'message': "Invalid wrestler"}, 400
        
@bp.route('/wrestler')
class WrestlerList(MethodView):
    
    @bp.response(200, WrestlerSchema(many = True))
    def get(self):
        return WrestlerModel.query.all()


    @bp.arguments(WrestlerSchema)
    def post(self, wrestler_data):
        try:
            wrestler = WrestlerModel()
            wrestler.commit()
            return {"message" : f'{wrestler_data["athlete"]} created'}, 201
        except:
            abort(400, message = "that wrestler is already entered")
        