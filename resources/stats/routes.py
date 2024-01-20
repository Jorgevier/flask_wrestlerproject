from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity
from uuid import uuid4
from flask.views import MethodView
from flask_smorest import abort

from models import StatModel

from schemas import StatSchema, StatSchemaNested

from . import bp



@bp.route('/<post_id>')
class Stat(MethodView):

    @bp.response(200, StatSchemaNested)
    def get(self, stat_id):
        stat = StatModel.query.get(stat_id)
        if stat:
            return stat
        abort(400, message='Invalid post')

    @bp.arguments(StatSchema)
    def put(self,stat_data, stat_id):
        stat = StatModel.query.get(stat_id)
        if stat:
            stat.body = stat_data['body']
            stat.commit()
            return { 'message': 'stat has been updated' }, 202
        return {'message': "Invalid stat id"}, 400


# @bp.delete('/post/<stat_id>')
    def delete(self, stat_id):
        stat = StatModel.query.get(stat_id)
        if stat:
            stat.delete()
            return {"message": "stat is deleted"}, 202
        return {'message':"Invalid stat"}, 400
        
@bp.route('/')
class StatList(MethodView):

    # @bp.get('/stat')
    @bp.response(200, StatSchema(many = True))
    def get(self):
        return StatModel.query.all()
    
    # @bp.stat('/stat')
    @jwt_required()
    @bp.arguments(StatSchema)
    def stat(self, stat_data):
        try:
            stat = StatModel()
            stat.wrestler_id = get_jwt_identity
            stat.body = stat_data['body']
            post.commit()
            return { 'message': "New Stat Created" }, 201
        except:
            return { 'message': "Invalid User"}, 401

