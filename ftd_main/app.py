# app.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os.path import abspath

db_folder = abspath("ftd_main/fixed_deposit.db")

db_location =  "".join(["sqlite:////", db_folder])

print("\n\n*******", db_location)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = db_location
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.secret_key = "fixedDepositsRocks!"

db = SQLAlchemy(app)


