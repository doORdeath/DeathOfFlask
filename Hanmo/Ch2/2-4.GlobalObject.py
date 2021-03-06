from flask import g, Flask
import sqlite3

app = Flask(__name__)

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

@app.before_request
def before_request():
    g.db = connect_db()


@app.teardown_request
def teardown_request(exception):
    db = getattr(g,'db',None)
    if db is not None:
        db.close()

@app.route("/")
def helloworld():
    return "Hello World"

if __name__=="__main__":
    app.run()
