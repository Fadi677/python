from  flask import Flask , render_template  
app = Flask(__name__)

@app.route('/')                           
def Checker_Board():
    return render_template('index.html')  

@app.route('/lists')
def render_lists():
    # Soon enough, we'll get data from a database, but for now, we're hard coding data
    users = [
            {'first_name' : 'Michael', 'last_name' : 'Choi'},
            {'first_name' : 'John', 'last_name' : 'Supsupin'},
            {'first_name' : 'Mark', 'last_name' : 'Guillen'},
            {'first_name' : 'KB', 'last_name' : 'Tonel'}
            ]
    return render_template("index.html", students = users)

# @app.route('/<int:number>')
# def display(number):
#     return render_template('check.html', times=number)

# @app.route('/<int:number2>/<int:number>')
# def display2(number2,number):
#     return render_template('check3.html', times=number,times2=number2)

if __name__=="__main__":
    app.run(debug=True)              