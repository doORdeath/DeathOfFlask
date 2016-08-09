from flask import Flask,g


app = Flask(__name__)

@app.route("/fuck")
def helloworld():
    return "Hello World"

@app.route("/")
def aaa():
    return "aaaa"

app.run(host="0.0.0.0")
