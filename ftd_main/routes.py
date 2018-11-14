from ftd_main import app, db
from ftd_main.models import FixedDeposit
from ftd_main.forms import AddFixedDepositForm, create_deposit, SubmitField
from flask import flash, render_template, request, redirect, url_for

@app.route('/')
@app.route('/index')
def index():

    user = {"username": 'Tampopo'}
    return render_template('index.html', title='Home', user=user)

@app.route('/new_deposit', methods=['GET', 'POST'])
def new_deposit():
    """
    Add a new deposit
    """
    form = AddFixedDepositForm()

    if form.validate_on_submit():
        # save the deposit
        deposit = FixedDeposit()
        new_deposit = create_deposit(deposit, form, new=True)
        db.session.add(new_deposit)
        db.session.commit()

        flash('New Fixed Deposit created successfully!')
        return redirect(url_for('index'))

    return render_template('new_deposit.html',  title='Add Deposit', form=form)
