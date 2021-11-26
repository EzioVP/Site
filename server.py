import sqlite3
from flask import Flask, render_template, request
import bancodedados


app = Flask(__name__)


@app.route("/")
def home():
    return render_template('/home.html')

 #botao entrar
@app.route("/entrar", methods=["POST"])
def entrar():
    return render_template('login.html')

 

#template
@app.route("/entrar")
def login():
    return render_template('login.html')

@app.route("/profissionaisdisponiveis")
def profissionaisdisponiveis():
    return render_template('profissionaisdisponiveis.html')

#botão serviços disponiveis   
@app.route("/servicosdisponiveis", methods=["POST"])
def servicos():
    return render_template('servicosdisponiveis.html')

#botão home   
@app.route("/", methods=["POST"])
def bhome():
    return render_template('home.html')

#template
@app.route("/servicosdisponiveis")
def servicosdisponiveis():
    return render_template('servicosdisponiveis.html')  

#botão continuar
@app.route("/continuar", methods=["POST"])
def continuar():
    return render_template('profissionaisdisponiveis.html')

@app.route("/registranobancodedados", methods=["POST","GET"])
def registranobancodedados():
    conn=sqlite3.connect('usuarios.db')
    Nome = request._load_form_data("Nome")
    Bairro = request.form["Bairro"]
    Telefone = request.form["Telefone"]
    Senha = request.form["Senha"]
    bancodedados.cursor.execute(""" 
    INSERT INTO usuarios(Nome, Bairro, Telefone, Senha) VALUES(?, ?, ?, ?)
    """, (Nome, Bairro, Telefone, Senha))
    bancodedados.conn.commit()
    



if __name__ == "__main__":
    app.run(debug=True)

