from flask import Flask, render_template
app= Flask (__name__)
@app.route('/play')
def index():
    return render_template("playground.html")
@app.route('/play/<int:x>')
def boxes(x):
    return render_template("playground-x.html",number = x)
@app.route('/play/<int:x>/<color>')
def colorme(x,color):

    return render_template("playground-x.html",number=x, colorbox=color)


if __name__=="__main__":
    app.run(debug=True)