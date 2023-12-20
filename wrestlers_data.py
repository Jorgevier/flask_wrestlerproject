from flask import Flask, request
from uuid import uuid4

app = Flask(__name__)

wrestlers = {
  '1': {
    'name': 'Steve Austin',
    'nickname' : 'Stone Cold',
    'billing from' : 'Victoria, Texas'
  },
  '2' : {
    'name': 'Bret Hart',
    'nickname' : 'Hitman',
    'billing from' : 'Calgary, Canada'
  }
}

stats = {
  '1' : {
    'signature_moves' : 'Stunner',
    'user_id': '1'
  },
  '2': {
    'signature_moves': 'Sharp Shooter',
    'user_id': '2'
  }
  
}

""" 
Create - Post
Retrieve - Get
Update 
Delete
 """


# user routes

@app.get('/wrestler')
def wrestlers():
  return { 'wrestlers': list(wrestlers.values()) }, 200

@app.route('/wrestler', methods=["POST"])
def create_wrestler():
  json_body = request.get_json()
  wrestlers[uuid4()] = json_body
  return { 'message' : f'{json_body["wrestler"]} created' }, 201

@app.put('/wrestler')
def update_wrestler():
  return

@app.delete('/wrestler')
def delete_wrestler():
  pass

# post routes

@app.get('/stat')
def get_stats():
  return

@app.post('/stat')
def create_stat():
  return

@app.put('/stat')
def update_stat():
  return

@app.delete('/stat')
def delete_stat():
  return