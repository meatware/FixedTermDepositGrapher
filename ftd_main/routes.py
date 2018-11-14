from ftd_main import app, db
from ftd_main.models import FixedDeposit
from ftd_main.forms import AddFixedDepositForm, create_deposit
from flask import flash, render_template, request, redirect

@app.route('/')
@app.route('/index')
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
        new_deposit = create_deposit(deposit, form, new=True)
        db.session.add(new_deposit)
        db.session.commit()

        flash('New Fixed Deposit created successfully!')
        return redirect('/')

    return render_template('new_deposit.html', form=form)
