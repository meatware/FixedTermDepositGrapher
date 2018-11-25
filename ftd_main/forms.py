from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, DecimalField, IntegerField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, NumberRange, Length, ValidationError, DataRequired, Email, EqualTo
from ftd_main.models import User


#TODO: fix form flashing
class AddFixedDepositForm(FlaskForm):
    ischemes = [('Monthly', 'Monthly'),
               ('Quarterly', 'Quarterly'),
               ('Yearly', 'Yearly')]

    ac_no = StringField('Acc No', validators=[DataRequired(), Length(5, 50, "Length range from 5 to 50")]) # TODO: Fix so autoincrements for user
    start_date = StringField('Start Date dd/mm/yyyy', validators=[DataRequired()]) #TODO: add validators
    end_date = StringField('End Date dd/mm/yyyy') #TODO: Calculate end_date
    interest_rate = DecimalField('Interest Rate (%)', validators=[DataRequired(), NumberRange(0, 100, "Please enter percentage range 0 to 100%")])
    interest_scheme = SelectField('Interest Scheme', choices=ischemes, validators=[DataRequired()])
    period = IntegerField('Deposit time period (days for now)')
    initial_deposit = DecimalField('Initial Deposit')
    final_deposit = DecimalField('Final Deposit') #TODO: Calculate final_deposit
    submit = SubmitField('Submits')

def create_deposit(deposit, form, new=False):
    """
    Save the changes to the database
    """
    # Get data from form and assign it to the correct attributes
    # of the SQLAlchemy table object

    deposit.ac_no = form.ac_no.data
    deposit.start_date = form.start_date.data
    deposit.end_date = form.end_date.data
    deposit.interest_rate = form.interest_rate.data
    deposit.interest_scheme = form.interest_scheme.data
    deposit.period = form.period.data
    deposit.initial_deposit = form.initial_deposit.data
    deposit.final_deposit = form.final_deposit.data

    return deposit

class Loginform(FlaskForm)    :
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')



