from flask import request
from uuid import uuid4
from flask.views import MethodView


from . import bp
from db import wrestlers
from schemas import WrestlerSchema


@bp.route('/wrestlers/<wrestler_id>')
class Wrestler(MethodView):

    @bp.response(200, WrestlerSchema)
# @app.get('/wrestlers/<wrestler_id>')
    def get(self, wrestler_id):
        try:
            return wrestlers[wrestler_id]  
        except:
            return {'message': 'invalid wrestler'}, 400

# @app.put('/wrestlers/<wrestler_id>')
    @bp.arguments(WrestlerSchema)
    def put(self, wrestler_data, wrestler_id):
        try:
            wrestler = wrestlers[wrestler_id]
            # wrestler_data = request.get_json()
            wrestlers |= wrestler_data
            return { 'message': f'{wrestlers["wrestlername"]} updated'}, 202
        except KeyError:
            return {'message': "Invalid info"}, 400
        
    def delete(self, wrestler_id):
        try:
            del wrestlers[wrestler_id]
            return { 'message': f'wrestler Deleted' }, 202
        except:
            return {'message': "Invalid wrestler"}, 400
        
@bp.route('/wrestler')
class WrestlerList(MethodView):
    
    @bp.response(200, WrestlerSchema(many = True))
    def get(self):
        return list(wrestlers.values())

# @app.delete('/wrestlers/<wrestler_id>')


    # @app.route('/wrestler', methods=["POST"])
    @bp.arguments(WrestlerSchema)
    def wrestler(self, wrestler_data):
        # wrestler_data = request.get_json()
        wrestlers[uuid4()] = wrestler_data
        return { 'message' : f'{wrestler_data["wrestler"]} created' }, 201