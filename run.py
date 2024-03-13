from flask import Flask

app = Flask(__name__)

@app.route('/')
def angel():
    return '<center><h1>5to informatica</h1></center>'

@app.route('/home/<name>')
def home(name):
    return f'Esto es una pagina web de {name}'

@app.route("/login/<name>")
def login(name):
    return f'Bienvenido {name}'

if __name__ == '__main__':
    app.run(debug = True)