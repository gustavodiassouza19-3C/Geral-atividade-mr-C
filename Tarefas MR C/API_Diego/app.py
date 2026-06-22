from flask import Flask
from datetime import date
app = Flask (__name__)

data_atual = date.today()


@app.route("/")
def inicio():
    return "bem vindo"

@app.route("/nome")
def nome():
    return"Meu nome é gustavo aurinha dambros dias de souza"

@app.route("/curso")
def curso():
    return"meu curso é o de desenvolvimento de sistemas"

@app.route("/escola")
def escola():
    return"Minha escola é o grande ceep pedro boareto neto"
    
@app.route("/hello")
def ola():
    return"Muitos olás cidadão"


@app.route("/date")
def data():
    return str(data_atual)
    

if __name__ == "__main__":
    app.run(debug=True)