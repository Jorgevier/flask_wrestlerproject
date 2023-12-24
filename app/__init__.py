from flask import Flask
from flask_smorest import Api
from Config import Config

app = Flask(__name__)
app.config.from_object(Config)
api = Api(app)

from resources.wrestler import bp as wrestler_bp
api.register_blueprint(wrestler_bp)

from resources.stat import bp as stat_bp
api.register_blueprint(stat_bp)
