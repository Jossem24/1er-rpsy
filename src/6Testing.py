from flask import Flask, render_template

app = Flask(__name__)
@app.route("/nomes")
def nomes():
    lista_nomes = ["jose", "maria", "joao"]
    return render_template("nomes.html", nomes=lista_nomes)

if __name__ == "__main__":
    app.run()