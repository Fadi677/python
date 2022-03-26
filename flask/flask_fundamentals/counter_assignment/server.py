from multiprocessing import reduction
from flask import Flask, render_template, request, redirect,session
app= Flask (__name__)
app.secret_key='secrets'

@app.route('/')
def count():
    return redirect('/visits')

@app.route('/destroy_session',methods=['POST'])
def clearcount():
    session.pop('counts')
    return redirect('/')

@app.route('/visits')
def visits_count():
    if 'counts' not in session:
        session['counts'] = 1
        print( session['counts'])
        print("key 'key_name' does NOT exist")
    else:
        print('key exists!')
        session['counts'] += 1 #session['count'] = session['counts'] +1
        print( session['counts'])
    return render_template('counter.html')

if __name__ == "__main__":
    app.run(debug=True)