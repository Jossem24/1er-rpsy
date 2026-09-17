import sqlite3
from flask import Flask, render_template,request, redirect, url_for

app = Flask(__name__)
def banco_novo():
   conexao = sqlite3.connect("validacao.db")
   cursor = conexao.cursor()

   cursor.execute(
        "CREATE TABLE IF NOT EXISTS usuarios"
        "(id INTEGER PRIMARY KEY AUTOINCREMENT,"
        "nome TEXT,"
        "idade INTEGER)"
   )
   conexao.commit()
   conexao.close()
@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    if request.method == "POST":
      nome = request.form.get("nome", "").strip()
      idade_texto = request.form.get("idade", "").strip()

      if not nome:
        mensagem = "Digite um nome"
        return render_template("cadastro.html", mensagem=mensagem)

      try :
         idade = int(idade_texto)
      except ValueError:
         mensagem = "Idade Invalida"
         return render_template("cadastro.html", mensagem=mensagem)

      if idade < 0 or idade >120:
         mensagem = "Idade fora do intervalo"
         return render_template("cadastro.html", mensagem=mensagem)
   
      conexao = sqlite3.connect("validacao.db")
      cursor = conexao.cursor()
      cursor.execute(

         "INSERT INTO usuarios (nome, idade) VALUES (?,?)",
         (nome, idade),
      )
      conexao.commit()
      conexao.close()
      return redirect(url_for("usuarios"))
    return render_template("cadastro.html")


@app.route("/usuarios")
def usuarios():
   conexao = sqlite3.connect("validacao.db")
   cursor = conexao.cursor()

   cursor.execute(

       "SELECT nome, idade FROM usuarios"
   )

   dados = cursor.fetchall()
   conexao.close()
   return render_template("usuarios.html", dados=dados)
if __name__=="__main__":
   banco_novo()
   app.run()
   