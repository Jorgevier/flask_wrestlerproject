from flask import request
from uuid import uuid4

from app import app
from db import stats, wrestlers

@app.get('/stat')
def get_stats():
  return { 'stats': list(stats.values()) }

@app.get('/stat/<stat_id>')
def get_stat(stat_id):
  try:
    return {'stat': stats[stat_id]}, 200
  except KeyError:
    return {'message': "Invalid stat"}, 400

@app.stat('/stat')
def create_stat():
  stat_data = request.get_json()
  wrestler_id = stat_data['wrestler_id']
  if wrestler_id in wrestlers:
    stats[uuid4()] = stat_data
    return { 'message': "New Stat Created" }, 201
  return { 'message': "Invalid User"}, 401

@app.put('/stat/<stat_id>')
def update_stat(stat_id):
  try:
    stat = stats[stat_id]
    stat_data = request.get_json()
    if stat_data['wrestler_id'] == stat['wrestler_id']:
      stat['body'] = stat_data['body']
      return { 'message': 'stat has been updated' }, 202
    return {'message': "Unauthorized"}, 401
  except:
    return {'message': "Invalid stat id"}, 400


@app.delete('/post/<stat_id>')
def delete_stat(stat_id):
  try:
    del stats[stat_id]
    return {"message": "stat is deleted"}, 202
  except:
    return {'message':"Invalid stat"}, 400