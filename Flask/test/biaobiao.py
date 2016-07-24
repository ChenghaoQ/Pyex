from flask import Flask


app=Flask(__name__)

@app.route('/')
def biaobiao():
        return '表表是个大傻蛋'


if __name__ == '__main__':
        app.run()
