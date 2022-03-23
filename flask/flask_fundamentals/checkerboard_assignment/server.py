from  flask import Flask , render_template  
app = Flask(__name__)

@app.route('/')                           
def Checker_Board():
    return render_template('checkerboard.html')  

@app.route('/<int:number>')
def display(number):
    return render_template('check.html', times=number)

@app.route('/<int:number2>/<int:number>')
def display2(number2,number):
    return render_template('check3.html', times=number,times2=number2)

if __name__=="__main__":
    app.run(debug=True)                  