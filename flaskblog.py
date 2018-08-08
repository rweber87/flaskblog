from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '10b518947411cb51f2fac2cc453e3452'

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

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
	app.run(debug=True)


