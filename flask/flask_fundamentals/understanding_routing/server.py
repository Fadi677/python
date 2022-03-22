from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/dojo')         
def dojo():
    return 'Dojo!'

@app.route('/say/<name>')         
def saysth(name):
    return "Hi " + name

@app.route('/repeat/<int:repeat>/<textme>')         
def repeatme(repeat,textme):
    if isinstance(repeat, int):
        return textme*int(repeat)
    else:
        return "please enter an integer as a repeat value"
        


if __name__=="__main__":
    app.run(debug=True)