import os
from flask import send_from_directory
from ftd_main import create_app
from flask_login import current_user, login_user, logout_user, login_required
from ftd_main.models import db, FixedDeposit, User
from ftd_main.forms import AddFixedDepositForm, Loginform, RegistrationForm, create_deposit
from flask import flash, render_template, request, redirect, url_for
from werkzeug.urls import url_parse

# init app
app = create_app()

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static/img'),
                          'favicon.ico',mimetype='image/vnd.microsoft.icon')

@app.route('/register', methods=['GET', 'POST'])
def register():
    try:
        if current_user.is_authenticated:
            return redirect(url_for('index'))
        form = RegistrationForm()

        if form.validate_on_submit():
            user = User(username=form.username.data, email=form.email.data)
            user.set_password(form.password.data)
            db.session.add(user)
            db.session.commit()
            flash('Congratulations, you are now a registered user!')
            return redirect(url_for('login'))
    except Exception as e:
        flash(f'Error - {str(e)}') #TODO: Create error logs
    
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = Loginform()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()

        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))

        login_user(user, remember=form.remember_me.data)

        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)

    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/')
@app.route('/index')
@login_required
def index():
    #TODO: add featre to show users last N deposits
    #user = {"username": 'Tampopo'}
    return render_template('index.html', title='Home')

@app.route('/new_deposit', methods=['GET', 'POST'])
@login_required
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
