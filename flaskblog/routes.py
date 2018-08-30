from flask import render_template, url_for, flash, redirect
from flaskblog import app
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post

posts = [
	{
		'author': 'Robbie Weber',
		'title': 'Blog Post 1',
		'content': 'First blog content',
		'date_posted': 'July 31, 2018'
	},
	{
		'author': 'Robbie Weber',
		'title': 'Blog Post 2',
		'content': 'Second blog content',
		'date_posted': 'August 1, 2018'
	}
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
    	flash('Account created for %s!' %form.username.data, 'success')
    	return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
	    if form.email.data == 'admin@blog.com' and form.password.data == 'password':
	    	flash('%s has successfully logged in!' %form.email.data, 'success')
	    	return redirect(url_for('home'))
	    else:
	    	flash('Login Unsuccessful. Please check username or password!', 'danger')
    return render_template('login.html', title='Login', form=form)