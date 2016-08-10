#Response 클래스 종류에 따른 사용

from flask import Response, make_response,Flask

app=Flask(__name__)

@app.route("/response_class")
def response_test():
    custom_response = Response("Custom Response",200,{
        "Program" : "Flask Wep Application"
    })

    return make_response(custom_response)


@app.route("/str")
def response_test_str():
    return make_response("Custom Response")

@app.route("/unicode")
def response_test_unicode():
    return make_response(u"Custom Response")

@app.route("/WSGIfunction")
def custom_response_WSGI():
    #WSGI를 사용하면 보다 정교한 HTTP응답 제어가 가능
    def application(environ, start_response):
        response_body = 'The request method was %s'%environ['REQUEST_METHOD']

        status = '200 OK'
        response_headers = [('Content-Type','text/plain'),('Content-Length',str(len(response_body)))]

        start_response(status,response_headers)

        return [response_body]
    return make_response(application)

@app.route("/tuple")
def custom_response_tuple():
    #응답코드, 상태코드, 응답 헤더
    return make_response(('Tuple Custom Response', 'OK',{
        'response_method' : 'Tuple Response'
    }))

app.run()