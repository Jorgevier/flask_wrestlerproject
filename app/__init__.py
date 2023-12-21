from flask import Flask

app = Flask(__name__)

from resources.stats import routes
from resources.wrestlers import routes