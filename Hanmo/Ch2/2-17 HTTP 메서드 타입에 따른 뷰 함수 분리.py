from flask import Flask

app= Flask(__name__)

@app.route('/board',methods=['GET'])
def board_list_get():
    pass

@app.route('/board',methods=['POST'])
def board_list_post():
    pass

#GET, POST 같이
#오류나면 망하기 떄문에 신중해야함 ;
@app.route('/board',methods=['GET','POST'])
def board_list():
    pass

#url_for함수에서 뷰함수 식별하기 위한 별칭을 지정
@app.route('/board',endpoint="board")
def board():
    pass


#동적으로 변경되는 URL의 뷰 함수 선언하기
#URL주소에 변수를 추가하기 위해서 <>를 사용
@app.route('/board/<article_idx>')
def board_view(article_idx):
    pass

#URL변수에 기본값 할당
@app.route('/board',defaults={'page':'inddex'})
@app.route('/board/<page>')
def board_page(page):
    pass

if __name__=="__main__":
    app.run()
