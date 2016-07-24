from flask import Flask
app = Flask(__name__)


@app.route('/sum/<int:post_1>/<int:post_2>')

def show_post(post_1,post_2):
        result=post_1+post_2
        return str(result)
        #return str(int(post_1)+int(post_2))


if __name__ == '__main__':
        app.run()
