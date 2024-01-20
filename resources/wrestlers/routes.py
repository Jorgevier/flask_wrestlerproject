from flask import request

from flask.views import MethodView
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_smorest import abort

from . import bp
from db import wrestlers

from schemas import WrestlerSchema, WrestlerSchemaNested
from models.wrestler_models import WrestlerModel


@bp.route('/wrestlers/<wrestler_id>')
class Wrestler(MethodView):

    @bp.response(200, WrestlerSchema)
    def get(self, wrestler_id):
        wrestler = WrestlerModel.query.get(wrestler_id)
        if wrestler:
            print(wrestler.posts.all())
            return wrestler  
        else:
            abort (400, message="that wrestler is not found")

    @jwt_required()
    @bp.arguments(WrestlerSchema)
    def put(self, wrestler_data, wrestler_id):
        wrestler = WrestlerModel.query.get(get_jwt_identity())
        if wrestler and wrestler_id:
            wrestler.from_dict(wrestler_data)
            wrestlers.commit()
            return { 'message': f'{wrestlers.athlete} updated'}, 202
        abort (400, message="invalid user")

    @jwt_required()   
    def delete(self, wrestler_id):
        wrestler = WrestlerModel.query.get(get_jwt_identity())
        if wrestler == wrestler_id:
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

@bp.route('/user/follow/<followed_id>')
class FollowUser(MethodView):
    
    @jwt_required()
    def stat(self, managed_id):
        managed = WrestlerModel.query.get(managed_id)
        manager =WrestlerModel.query.get(get_jwt_identity())
        if manager and managed:
            manager.follow(managed)
            managed.commit()
            return {'message':' managed'}
        else:
            return {'message':'invalid manager'}, 400
        
    @jwt_required()  
    def put(self, managed_id):
        managed = WrestlerModel.query.get(managed_id)
        manager = WrestlerModel.query.get(get_jwt_identity())
        if manager and managed:
            manager.unfollow(managed)
            managed.commit()
            return {'message':'user not managed'}
        else:
            return {'message':'invalid manager'}, 400


        