from flask import render_template
from app import app
@app.route('/')
@app.route('/index')

def index():
#1        return "Hello world!"
#2        user={'nickname':'Miguel'}
#2        return render_template("index.html",title="Home", user = user) 
	user= {'nickname':'Miguel'}
	posts =[#提交内容
		{
		'author':{'nickname':'John'},
		'body':'Beautiful day in Portland!'
		},
		{
			'author':{'nickname':'Susan'},
			'body':'The Avengers movie was so cool!'
		}
		
		]
	return render_template("index.html",title = 'Home', user =user,posts=posts)
