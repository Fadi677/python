from flask import Flask, render_template, request, redirect,session
app= Flask (__name__)
app.secret_key='this is a secret key'

@app.route('/')
def index():
    if session:
        print(session)
        session.clear()
        print(session)
    
    return render_template("form.html")

@app.route('/result',methods=['POST'])
def submitme():
    session['name']=(request.form['name'])
    session['location']=(request.form['location'])
    session['language']=(request.form['language'])
    session['comment']=(request.form['comment'])
    return redirect('/show')

@app.route('/show')
def showinfo():
    return render_template('result.html')








if __name__ == "__main__":
    app.run(debug=True)