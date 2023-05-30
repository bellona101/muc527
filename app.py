from flask import Flask,render_template

app = Flask(__name__)


@app.route('/a')
def area():  # put application's code here
    return render_template("area-pieces.html")

@app.route('/index.html')
def index():  # put application's code here
    return render_template("index.html")

@app.route('/time.html')
def time():  # put application's code here
    return render_template("time.html")

@app.route('/bar-data-color.html')
def bar():  # put application's code here
    return render_template("bar-data-color.html")

@app.route('/item.html')
def item():  # put application's code here
    return render_template("item.html")

@app.route('/word.html')
def word():  # put application's code here
    return render_template("word.html")



if __name__ == '__main__':
    app.run()
