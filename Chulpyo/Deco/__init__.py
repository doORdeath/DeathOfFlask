__author__ = 'Chulpyo'


class app:
    class deco:
        def __init__(self, f):
            app.func = f

        def __call__(self):
            app.func()


@app.deco
def myfunc():
    print("test2")


app.func()
#myfunc()
