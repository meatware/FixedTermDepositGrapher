# main.py

from ftd_main.app import app
from ftd_main.db_setup import init_db, db_session
from ftd_main.forms import AddFixedDepositForm
from flask import flash, render_template, request, redirect
from ftd_main.models import FixedDeposit

init_db()

def save_changes(deposit, form, new=False):
    """
    Save the changes to the database
    """
    # Get data from form and assign it to the correct attributes
    # of the SQLAlchemy table object
    deposit = FixedDeposit()

    deposit.ac_no = form.ac_no.data
    deposit.start_date = form.start_date.data
    deposit.end_date = form.end_date.data
    deposit.interest_rate = form.interest_rate.data
    deposit.interest_scheme = form.interest_scheme.data
    deposit.period = form.period.data
    deposit.initial_deposit = form.initial_deposit.data
    deposit.final_deposit = form.final_deposit.data

    if new:
        # Add the new deposit to the database
        db_session.add(deposit)

    # commit the data to the database
    db_session.commit()

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/new_deposit', methods=['GET', 'POST'])
def new_deposit():
    """
    Add a new deposit
    """
    form = AddFixedDepositForm(request.form)

    if request.method == 'POST' and form.validate():
        # save the album
        deposit = FixedDeposit()
        save_changes(deposit, form, new=True)
        flash('New Fixed Deposit created successfully!')
        return redirect('/')

    return render_template('new_deposit.html', form=form)

if __name__ == '__main__':
    app.run()

