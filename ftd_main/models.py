from ftd_main import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(UserMixin, db.Model):
    __tablename__ = "user"

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    deposits =db.relationship('FixedDeposit', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)


class FixedDeposit(db.Model):
    __tablename__ = "deposits"

    id = db.Column(db.Integer, primary_key=True) #TODO: change to acc_no?
    ac_no = db.Column(db.String)
    start_date = db.Column(db.String) #db.DateTime, index=True)
    end_date = db.Column(db.String) #, index=True)
    interest_rate = db.Column(db.Float)
    interest_scheme = db.Column(db.String)
    period = db.Column(db.Integer)
    initial_deposit = db.Column(db.Float)
    final_deposit = db.Column(db.Float)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return "<FixedDeposit: {}>".format(self.ac_no + str(self.user_id))
