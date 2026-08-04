from flask import (
    Flask,
    redirect,
    render_template,
    request,
    session,
    url_for,
)
        
app = Flask(__name__)
app.secret_key = "chave-apenas-para-estudo" #.secret_key : espaço onde guardamos a chave secreta

@app.route("/login", methods=["GET", "POST"]) # GET mostra form, POST recebe/envía dados
def login():
    erro = None

    if request.method == "POST":
        usuario = request.form["usuario"] #primeira declaração da variavel USUARIO, e ela é digitada no formulario pelo usuario
                                          #e ali depois se cria o if de embaixo que pede que o valor de usurio seja Jose para a if se executar
        senha = request.form["senha"]

        if usuario == "jose" and senha == "1234": #verifica se as credenciais (jose e 1234)são corretas
            session["usuario"] = usuario #guarde na sessão (session), no espaço chamado (["usuario"]) o valor da var (usuario) usuario
            return redirect(url_for("painel")) #encontre a url a função painel (url_for("painel")), mande ao usu a outra pag (redirect) retorne tudo isso (return)

        erro = "Usuário ou senha incorretos" # se as credenciais não são corretas

    return render_template("login.html", erro=erro) #é do primeiro if, se as credencias não são corretas

@app.route("/painel")
def painel():
    if "usuario" not in session: #se o usuario não estiver logado
        return redirect(url_for("login")) #manda (redirect) para o login

    return render_template(         #se entrar mostra o painel (A bemvinda)
        "painel.html",
        usuario=session["usuario"], #pega o nome guardado em session["usuario"(o USUARIO)]
    )


@app.route("/logout") # esta ruta se usa diretamente no html para o navegador encerrar session do usuario
def logout():
    session.pop("usuario", None) #remove ao usuario atual da session (session.pop)
    return redirect(url_for("login")) #redirige ao login


if __name__ == "__main__":
    app.run(debug=True)