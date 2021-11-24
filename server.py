from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/home")
def home():
    return render_template('/home.html')

 #botao entrar
@app.route("/entrar", methods=["POST"])
def entrar():
    return render_template('login.html')

#botão continuar
@app.route("/continuar", methods=["POST"])
def continuar():
    return render_template('profissionaisdisponiveis.html') 

#template
@app.route("/login")
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
@app.route("/home", methods=["POST"])
def bhome():
    return render_template('home.html')

#template
@app.route("/servicosdisponiveis")
def servicosdisponiveis():
    return render_template('servicosdisponiveis.html')


if __name__ == "__main__":
    app.run(debug=True)

