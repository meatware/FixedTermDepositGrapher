from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
#from flask_datepicker import datepicker

### Create App
app = Flask(__name__)
app.config.from_object(Config)

### Create database
db = SQLAlchemy(app)
migrate = Migrate(app, db)
#
login = LoginManager(app)
login.login_view = 'login'
#
#date_pick = datepicker(app)


### package imports
from ftd_main import routes, models
