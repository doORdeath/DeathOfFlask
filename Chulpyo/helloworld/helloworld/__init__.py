__author__ = 'Chulpyo'

from werkzeug.routing import BaseConverter
from flask import Flask, g, Response, make_response, url_for
import urllib
import sqlite3

# Flask Class 인자
# import_name: 기본적으로 __name__ 변수를 사용
# static_url_path: 정적파일(css, resource, ...)등 폴더를 지정하는 변수
# static_folder: 서버 내부에서 사용하는 폴더 위치 변수
# template_folder: 뷰가 사용할 HTML 파일 위치

app = Flask(__name__)


@app.route("/")
def http_prepost_response():
    return "/"


@app.route("/str")
def custom_response():
    def application(environ, start_response):
        print(environ)
        print(start_response)
        response_body = 'The Request method was %s' % environ['REQUEST_METHOD']
        status = '200 OK'
        response_headers = [('Content-Type', 'text/plain'),
                            ('Content-Length', str(len(response_body)))]

        start_response(status, response_headers)

        return [response_body]
    return make_response(application)


# def ch2_11_response():
#     def application(environ, start_response):
#         response_body = 'The Request method was %s' % environ['REQUEST_METHOD']
#         status = '200 OK'
#         response_headers = [('Content-Type', 'text/plain'),
#                             ('Content-Length', str(len(response_body)))]
#
#         start_response(status, response_headers)
#
#         return [response_body]
#     return make_response(application)


# code 2-16

@app.route('/board/<idx>')
def board_list(idx):
    return make_response(idx)


@app.route('/board2', redirect_to='/new_board')
def board2():
    return "리디렉션됩니다!"


@app.route("/new_board")
def board3():
    return "GOOD"


# code 2-32
def redirect_new_board(adapter, id1, id2):
    print(adapter)
    return "/new_board2/{0}/{1}".format(id1, id2)


@app.route('/board3/<id1>/<id2>', redirect_to=redirect_new_board)
def board(id1, id2):
    return "줮까!~"


@app.route('/new_board2/<id1>/<id2>')
def new_board2(id1, id2):
    return "{0}, {1} : GOOD?".format(id1, id2)


# @app.before_first_request
# def before_first_request():
#     print("앱이 가동되고 나서 첫 번째 HTTP 요청에 대한 응답.")
#
#
# @app.before_request
# def before_request():
#     print("매 http 요청이 처리되기 전에 실행.")
#
#
# @app.after_request
# def after_request(response):
#     print("매 http 요청이 처리된 후 실행.")
#
#
# @app.teardown_request
# def teardown_request(exception):
#     print("매 http 요청의 결과가 브라우저에 응답하고 나서 호출.")
#
#
# @app.teardown_appcontext
# def teardown_appcontext(exception):
#     print("Http 요청의 애플리케이션 컨택스트가 종료될때 실행.")


# @app.route("/str")
# def custom_response():
#     def application(environ, start_response):
#         response_body = 'The Request method was %s' % environ['REQUEST_METHOD']
#         status = '200 OK'
#         response_headers = [('Content-Type', 'text/plain'),
#                             ('Content-Length', str(len(response_body)))]
#
#         start_response(status, response_headers)
#
#         return [response_body]
#
#     return make_response(application)


# def response_test():
#     custom_response = Response("Custom Response", 200, {
#         "Program": "Flask Web Application"
#     })
#
#     return make_response(custom_response)

# 책 진행을 위하여 주석 처리
# def helloworld():
#     return "Hello World"


# def connect_db():
#     return sqlite3.connect(app.config['DATABASE'])
#
#
# @app.before_request
# def before_request():
#     g.db = connect_db()
#
#
# @app.teardown_request
# def teardown_request(exception):
#     db = getattr(g, 'db', None)
#     if db is not None:
#         db.close()


