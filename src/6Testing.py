from flask import Flask, render_template

app = Flask(__name__)
@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/contato")
def contato():
     return render_template("contato.html")

@app.route("/produto")
def produto():
     return render_template("produto.html")

if __name__ == "__main__":
     app.run() 

