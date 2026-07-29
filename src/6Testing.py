from flask import Flask, render_template
app = Flask(__name__)
@app.route("/alunos")
def alunos():
    alunos_1 = [
         {"nome": "jose", "nota": 7},
         {"nome": "magus", "nota": 6},
         {"nome": "pacha", "nota": 8},
    ]

    return render_template("alunos.html", alunos_1=alunos_1)

if __name__ == "__main__":
    app.run()
        




    