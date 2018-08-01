from flask import Flask, render_template, url_for
app = Flask(__name__)

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

if __name__ == '__main__':
	app.run(debug=True)


