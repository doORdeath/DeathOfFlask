from flask import Flask,request

app= Flask(__name__)

@app.route("/board")
def board_list():
    return "쿼리 스트링 question 변수의 값은 {}입니다.".format(request.args.get('question'))
#wekzeug.datastructures.MultiDict 타입으로 저장됨

@app.route("/board2")
def board():
    article_id = request.args.get("article","1",int)
    return str(article_id)

@app.route("/board2",methods=["POST"])
def board2():
    article_id = request.form.get("article","1",int)
    return str(article_id)

@app.route("/board3",methods=["GET","POST"])
def board3():
    return request.values.get("question")

#default 반환하기
@app.route("/board4",methods=["GET","POST"])
def board4():
    return request.values.get("question","질문을 입력하세용")

#answer를 받았으면 기본값은 nono고 int로 반환해라!
@app.route("/board5",methods=["GET","POST"])
def board5():
    return request.values.get("answer","nono",type=int)

from datetime import datetime


#함수형으로 데이터 반환
def dateKoeanType(date_format):
    def translate(date_str):
        return datetime.strptime(date_str,date_format)
    return translate

@app.route("/board6", methods=["GET","POST"])
def board6():
    print(request.values.get("date","2015-02-09",type=dateKoeanType("%Y-%m-%d")))
    return "날짜는 콘솔을확인해 보세요"


#클래스형으로 데이터 반환
class dataKoreanType2:
    def __init__(self,format):
        self.format=format

    def __call__(self,*args,**kwargs):
        return datetime.strptime(args[0],self.format)

@app.route("/board7",methods=["GET","POST"])
def board7():
    print(request.values.get("date","2015-02-09",type=dataKoreanType2("%Y-%m-%d")))
    return "날짜는 콘솔을 확인하셈"




if __name__=="__main__":
    app.run()