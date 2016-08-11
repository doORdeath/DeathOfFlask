from flask import Flask, make_response

app = Flask(__name__)

@app.route("/")
def custom_response():
    # response_object , response_status , response_header
    return make_response(('This is message', '200', {
        'response_method': 'Tuple Response'
    }))


if __name__ == "__main__":
    app.run()
