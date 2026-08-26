import sqlite3
from flask import Flask, redirect, url_for, render_template, request


app = Flask(__name__)

def banco_novo():
    conexao = sqlite3.connect("crud.db")
    cursor = conexao.cursor()

    cursor.execute(
        "CREATE TABLE IF NOT EXISTS usuarios "
        "(id INTEGER PRIMARY KEY AUTOINCREMENT,"
        "nome TEXT,"
        "idade INTEGER)"
    )

    conexao.commit()
    conexao.close()

@app.route("/cadastro/", methods=["GET", "POST"])
def cadastro():
          if request.method == "POST":
            nome = request.form["nome"]
            idade = request.form["idade"]

            conexao = sqlite3.connect("crud.db")
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
      conexao = sqlite3.connect("crud.db")
      cursor = conexao.cursor()

      cursor.execute(
                " SELECT id, nome, idade FROM usuarios "        
      )
      dados = cursor.fetchall()
      conexao.close()

      return render_template("usuarios.html", dados=dados) 


if __name__ == "__main__":
      banco_novo()
      app.run()