from flask import Flask
from flask_smorest import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from Config import Config

app = Flask(__name__)
app.config.from_object(Config)
api = Api(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from resources.wrestlers import bp as wrestler_bp
api.register_blueprint(wrestler_bp)

from resources.stats import bp as stat_bp
api.register_blueprint(stat_bp)
