from flask import ( Flask, render_template, request, session, url_for, redirect)

app = Flask(__name__)
app.secret_key = "apenas-para-estudo"




@app.route("/login", methods=["GET", "POST"])
def login(): 
    if request.method == "POST":
       usuario = request.form["usuario"]
       senha = request.form["senha"]

       if usuario == "jose" and senha == "1234":
            session["usuario"] = usuario
            return redirect(url_for("painel"))
       else:
           mensagem = "Usuário ou senha incorretos" 
           return render_template("login.html", mensagem=mensagem )            
    return render_template("login.html")


@app.route("/painel")
def painel():
    if "usuario" not in session: #cuidado com usuario sem aspas, porque usuario é uma var da função login e "usuario" é um valor geral
        return redirect(url_for("login"))
    return render_template("painel.html", usuario = session["usuario"])


@app.route("/logout")
def logout ():
    session.pop("usuario", None)
    return redirect(url_for("login"))

if __name__ == "__main__":
     app.run()