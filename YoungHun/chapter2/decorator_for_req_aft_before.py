from flask import Flask

app = Flask(__name__)

@app.route("/")
def http_prepost_response():
    return "/"

@app.before_first_request
def before_first_requst():
    print("앱이 가동되고 나서 첫 번째 HTTP 요청에만 응답합니다")

@app.before_request
def before_request():
    print("매 HTTP 요청이 처리되기 전에 실행됩니다")

@app.after_request
def after_request(response):
    print("매 HTTP 요청이 처리된 후에 실행됩니다")
    return response

@app.teardown_request
def teardwon_request(exeption):
    print("매 HTTP요청의 결과가 브라우저에 응답하고 나서 호출됩니다")

@app.teardown_appcontext
def teardown_appcontext(exeption):
    print("HTTP 요청의 애플리케이션 컨텍스트가 종료될 때 실행합니다")

if __name__ == "__main__":
    app.run()