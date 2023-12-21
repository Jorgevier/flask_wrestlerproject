from flask import request
from uuid import uuid4

from app import app
from db import wrestlers

@app.get('/wrestler')
def wrestlers():
  return { 'wrestlers': list(wrestlers.values()) }, 200

@app.get('/wrestlers/<wrestler_id>')
def get_wrestler(wrestler_id):
  try:
    return { 'wrestlers': wrestlers[wrestler_id] } 
  except:
    return {'message': 'invalid wrestler'}, 400

@app.route('/wrestler', methods=["POST"])
def create_wrestler():
  wrestler_data = request.get_json()
  wrestlers[uuid4()] = wrestler_data
  return { 'message' : f'{wrestler_data["wrestler"]} created' }, 201

@app.put('/wrestlers/<wrestler_id>')
def update_wrestler(wrestler_id):
  try:
    wrestler = wrestlers[wrestler_id]
    wrestler_data = request.get_json()
    wrestlers |= wrestler_data
    return { 'message': f'{wrestlers["wrestlername"]} updated'}, 202
  except KeyError:
    return {'message': "Invalid info"}, 400


@app.delete('/wrestlers/<wrestler_id>')
def delete_wrestler(wrestler_id):
  try:
    del wrestlers[wrestler_id]
    return { 'message': f'wrestler Deleted' }, 202
  except:
    return {'message': "Invalid wrestler"}, 400
