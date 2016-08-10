from flask import Flask

app=Flask(__name__)
app.debug=True  #선택 1

#선택 2
app.config.update(
    DEBUG=True
)

