import os
basedir = os.path.abspath(os.path.dirname(__file__))

# Get db env from docker container
DB_SETTINGS = {
    'db_host' : os.getenv('HOST'),
    'db_user' : os.getenv('USER'),
    'db_pass' : os.getenv('PASSWORD'),
    'db_name' : os.getenv('DB_NAME'),
    'db_port' : os.getenv('PORT')
}

class Config(object):
    SECRET_KEY = os.environ.get('CSRF_SECRET') or 'fixedDepositsRocks!' #TODO: make secret key better
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{DB_SETTINGS["db_user"]}:{DB_SETTINGS["db_pass"]}@{DB_SETTINGS["db_host"]}/{DB_SETTINGS["db_name"]}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
