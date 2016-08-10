class Decoclass(object):
    def __init__(self,f):
        print ("데코레이터 클래스 시작")
        self.func =f;
    def __call__(self):
        print ("시작 : %s"%self.func.__name__)
        self.func()
        print("끝 : %s" % self.func.__name__)


@Decoclass
def inner_function():
    print ("내장된 함수 실행")

print ("프로그램 시작")
inner_function()