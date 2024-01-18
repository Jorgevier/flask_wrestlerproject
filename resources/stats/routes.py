from flask import request
from uuid import uuid4
from flask.views import MethodView

from schemas import StatSchema
from db import stats, wrestlers
from . import bp



@bp.route('/<post_id>')
class Stat(MethodView):

    @bp.response(200, StatSchema)
    def get(self, stat_id):
        try:
            return stats[stat_id]
        except KeyError:
            return {'message': "Invalid stat"}, 400

    @bp.arguments(StatSchema)
    def put(self,stat_data, stat_id):
        try:
            stat = stats[stat_id]
            if stat_data['wrestler_id'] == stat['wrestler_id']:
                stat['body'] = stat_data['body']
                return { 'message': 'stat has been updated' }, 202
            return {'message': "Unauthorized"}, 401
        except:
            return {'message': "Invalid stat id"}, 400


# @bp.delete('/post/<stat_id>')
    def delete(stat_id):
        try:
            del stats[stat_id]
            return {"message": "stat is deleted"}, 202
        except:
            return {'message':"Invalid stat"}, 400
        
@bp.route('/')
class PostList(MethodView):

    # @bp.get('/stat')
    @bp.response(200, StatSchema(many = True))
    def get(self):
        return list(stats.values()) 
    
    # @bp.stat('/stat')
    @bp.arguments(StatSchema)
    def stat(self, stat_data):
        wrestler_id = stat_data['wrestler_id']
        if wrestler_id in wrestlers:
            stats[uuid4()] = stat_data
            return { 'message': "New Stat Created" }, 201
        return { 'message': "Invalid User"}, 401

