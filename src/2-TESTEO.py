from flask import Flask, render_template,request

app = Flask(__name__)

@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    if request.method == "POST":
      nome = request.form.get("nome", "").strip()
      idade_texto = request.form.get("idade", "").strip()

      if not nome or not idade_texto:
        mensagem = "Digite un nome"
        return render_template("cadastro.html", mensagem=mensagem)

      try :
         idade = int(idade_texto)
      except ValueError:
         mensagem = "A idade precisa ser um numero"
         return render_template("cadastro.html", mensagem=mensagem)
    return render_template("cadastro.hmtl")

