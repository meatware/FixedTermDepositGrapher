from ftd_main import app, db
from ftd_main.models import User, FixedDeposit

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'FixedDeposit': FixedDeposit}
