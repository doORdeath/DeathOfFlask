from flask import Response, make_response, Flask

app = Flask(__name__)

a = 4

@app.route("/")
def response_test():
    custom_response = Response("Custom Response", 200, {
        "Program": "Flask Web Application"
    })
    return make_response(custom_response)

@app.route("/str")
def use_str():
    return str(a)

if __name__ == "__main__":
    app.run(host="0.0.0.0")