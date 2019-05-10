from flask import flash, redirect, url_for, render_template, Blueprint

from app import app, RegistrationForm, LoginForm

auth = Blueprint('auth', __name__, template_folder='templates')

@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash('Account created for {}!'.format(form.username.data), 'success')
        return redirect(url_for('dashboard.monitorDataList'))
    return render_template('register.html', title='Register', form=form)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "admin@blog.com" and form.password.data == "a":
            flash('You have been logged in', 'success')
            return redirect(url_for('dashboard.monitorDataList'))
        else:
            flash('Login failed. Check username and password.', 'danger')
    return render_template('login.html', title='Login', form=form)
