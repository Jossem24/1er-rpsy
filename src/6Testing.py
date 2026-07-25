from flask import Flask, render_template, request

app = Flask(__name__) #coloquei mal: aspas no name e f minuscula no flask
@app.route("/calculadora", methods=["GET", "POST"])#coloquei rn em vez de route, falto a coma depois de calculadora, faltaram as aspas no get e post

def calculadora():
    if request.method == "POST": #coloquei em {} e [] quando era so aspas
        num_1 = float(request.form["num_1"]) #esqueci do num_1 e num_2 nas aspas
        num_2 = float(request.form["num_2"])
        soma = (num_1 + num_2)
        resta = (num_1 - num_2)
        multi = (num_1 * num_2)
        media = (num_1 + num_2) / 2
        dados = {"num_1": num_1, "num_2": num_2, "soma": soma, "resta": resta, "multi": multi, "media": media}

        return render_template("resultado_calculadora.html", dados=dados)#o primer dados é o nome que html usará e o 2do é a variavel
    return render_template("mostragem.html")


if __name__ == "__main__":
    app.run()