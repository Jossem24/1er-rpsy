import sqlite3
from flask import Flask, render_template, url_for, redirect, request

app = Flask(__name__)

def criar_banco():
    conexao = sqlite3.connect("banco.db")
    cursor = conexao.cursor()

    cursor.execute (
              "CREATE TABLE IF NOT EXISTS usuarios"
              "(nome TEXT, idade INTEGER)"

    )

    conexao.commit()
    conexao.close()

@app.route("/cadastro", methods = ["GET", "POST"])
def cadastro():
    if request.method == "POST":
       nome = request.form["nome"]
       idade = request.form["idade"]

       conexao = sqlite3.connect("banco.db")
       cursor = conexao.cursor()

       cursor.execute(
            "INSERT INTO usuarios(nome, idade) VALUES (?,?)",
            (nome, idade),                       
 
       )       
       conexao.commit()
       conexao.close()

       mensagem = "Usuario Cadastrado"

       return render_template("cadastro.html", mensagem=mensagem)
    return render_template("cadastro.html") 


@app.route("/usuarios")

def usuarios():
    conexao = sqlite3.connect("banco.db")
    cursor = conexao.cursor()

    cursor.execute(
         "SELECT nome, idade FROM usuarios")
    dados = cursor.fetchall()
    conexao.close()

    return render_template("usuarios.html", dados=dados)


if __name__ == "__main__":
    criar_banco()
    app.run()
    
       
