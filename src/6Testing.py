from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/perfil", methods=["GET", "POST"])
def perfil():
    if request.method == "POST":
        nome = request.form["nome"]
        idade = request.form["idade"]
        cidade = request.form["cidade"]
        dados = {"nome": nome, "idade": idade, "cidade": cidade}
        return render_template("resultado.html",dados=dados)

    return render_template("perfil.html")


if __name__ == "__main__":
    app.run()