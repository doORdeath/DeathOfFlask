from flask import Flask

app =Flask(__name__)

#host 옵션
@app.route("/host", host="example.com")
@app.route("/host", host="example2.com")
def host():
    return "/host URL을 호출"

app.config['SERVER_NAME'] = 'example.com:5000'

#특정 도메인에 응답
@app.route("/board",subdomain="text")
def board_domain_test():
    return "Test 도메인의 /board URL호출"

@app.route("/board",subdomain="answer")
def board_domain_answer():
    return "Answer 도메인의 /board URL 호출"

#모든 도메인에 응답
@app.route("/board",subdomain="<user_domain>")
def board_domain_testandanswer(user_domain):
    return "{} 도메인의 /board URL을 호출하셨습니다".format(user_domain)

#리다이렉트 설정
@app.route("/board",redirect_to="/new_board")
def board():
    return "/new_board로 리다이렉트"

@app.route("/new_board")
def new_board():
    return "/new_board URL 호출"

#함수를 통한 리다이렉트
def redirect_new_board(adapter,id,id2):
    return "/new_board/{0}/{1}".format(id,id2)

@app.route("/board/<id>/<id2>",redirect_to=redirect_new_board)
def board(id,id2):
    return "호출안됨 ㅋ"

@app.route("/new_board/<id>/<id2>")
def new_board(id,id2):
    return "{0}, {1} 변수와 함께 new_board URL 호출".format(id,id2)



if __name__=="__main__":
    app.run()