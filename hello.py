from flask.ext.moment import Moment
from flask.ext.bootstrap import Bootstrap
from flask import render_template
from flask import  Flask

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    return render_template('base.html',name = 'caiyz'),201


if __name__=='__main__':
    app.run(debug=True)