from wtforms import Form, StringField, SelectField
 
class AddFixedDepositForm(Form):
    ischemes = [('Monthly', 'Monthly'),
               ('Quarterly', 'Quarterly'),
               ('Yearly', 'Yearly')]
               
    ac_no = StringField('Acc No')
    start_date = StringField('Start Date')
    end_date = StringField('End Date') #TODO: Calculate end_date
    interest_rate = StringField('Interest Rate (%)')
    interest_scheme = SelectField('Interest Scheme', choices=ischemes)
    period = StringField('Deposit time period (months)')
    initial_deposit = StringField('Initial Deposit')
    final_deposit = StringField('Final Deposit') #TODO: Calculate final_deposit
