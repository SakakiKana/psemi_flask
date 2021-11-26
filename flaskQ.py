from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    lis = []
    for i in range(0, 10):
        lis.append(i)
    dictionary = {"nickname": "sakaki", "age": 21, "address": "埼玉県"}
    flag = True
    return render_template('flaskQ.html', lis=lis, dictionary=dictionary, flag=flag)


if __name__ == "__main__":
    app.debug = True
    app.run(port=8000)
