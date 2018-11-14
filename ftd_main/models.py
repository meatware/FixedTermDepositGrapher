from ftd_main import db


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


    def __repr__(self):
        return "<FixedDeposit: {}>".format(self.ac_no + self.id)

