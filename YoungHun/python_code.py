class Verbose:
    def __init__(self, f):
        print("Initializing Verbose.")
        self.func = f

    def __call__(self):
        print("Begin", self.func.__name__)
        self.func()
        print("End", self.func.__name__)

class Line:
    def __init__(self, f):
        self.func = f

    def __call__(self):
        print("----------------")
        print(self.func.__name__)
        self.func()
        self.func()
        print("----------------")

@Verbose
def my_function():
    print("hello, world.")

@Line
def b():
    print("run")

my_function()
b()