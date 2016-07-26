from flask import Flask,render_template,url_for

app=Flask(__name__)

@app.route('/index')
def index():
        maincss=url_for("static",filename="css/main.css")
        return render_template('index.html',maincss=maincss)



if __name__=='__main__':
        app.run()
