from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

### Create App
app = Flask(__name__)
app.config.from_object(Config)

### Create database
db = SQLAlchemy(app)
migrate = Migrate(app, db)
#


### package imports
from ftd_main import routes, models
