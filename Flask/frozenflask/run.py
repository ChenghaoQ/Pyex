from app import app#orginal line
from flask_frozen import Freezer
freezer = Freezer(app)
if __name__ == '__main__':
	freezer.freeze()
#app.run(debug = True,port=9999)#original line
