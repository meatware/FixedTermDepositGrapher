# models.py

from ftd_main.app import db


class FixedDeposit(db.Model):
    __tablename__ = "deposits"

    id = db.Column(db.Integer, primary_key=True) #TODO: change to acc_no?
    ac_no = db.Column(db.String, unique=True)
    start_date = db.Column(db.String)
    end_date = db.Column(db.String)
    interest_rate = db.Column(db.String)
    interest_scheme = db.Column(db.String)
    period = db.Column(db.String)
    initial_deposit = db.Column(db.String)
    final_deposit = db.Column(db.String)


    def __repr__(self):
        return "<FixedDeposit: {}>".format(self.ac_no)


#class Album(db.Model):
#    """"""
#    __tablename__ = "albums"

#    id = db.Column(db.Integer, primary_key=True)
#    title = db.Column(db.String)
#    release_date = db.Column(db.String)
#    publisher = db.Column(db.String)
#    media_type = db.Column(db.String)
#
#    artist_id = db.Column(db.Integer, db.ForeignKey("artists.id"))
#    artist = db.relationship("Artist", backref=db.backref(
#        "albums", order_by=id), lazy=True)
