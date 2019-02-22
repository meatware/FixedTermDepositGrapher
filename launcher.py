from ftd_main.routes import app
from ftd_main.models import User, FixedDeposit, db

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'FixedDeposit': FixedDeposit}
