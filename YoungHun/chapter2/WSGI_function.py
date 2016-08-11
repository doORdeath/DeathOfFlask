from flask import Flask, make_response

app = Flask(__name__)

@app.route("/")
def custom_response():
    #WSGI function := application( environ dictionary that have the setting of web server enviroment,
    #                               function object for returnning of response to web browser s.t start_response)
    def application(environ, start_response):
        #create the string that returnning to browser
        #REQUEST_METHOD := 웹 브라우저가 URL을 어떤 메서드로 호출했는지 저장
        #                   environ 사전으로부터 참조함
        response_body = 'The request method was %s' % environ['REQUEST_METHOD']

        #응답 상태의 값 by code and message
        status = '200 OK'

        #응답메세지의 헤더를 작성
        # Content_Type := 응답하는 문자열이 Plain Text 문자열임을 알림
        # Content_Length := 응답하는 문자열의 길이를 알림
        response_headers = [('Content-Type', 'textplain'),
                            ('Content_Length', str(len(response_body)))]

        #start_response 함수 객체에 HTTP 응답 상태 코드와 HTTP 응답 해더를 전달해서 웹 브라우저에 응답을 시작
        start_response(status, response_headers)

        return [response_body]

    return make_response(application)

if __name__ == "__main__":
    app.run()