# terceiro exemplo de uma biblioteca - Flask:

# pip install flask - PARA INSTALAR A BILBIOTECA

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"