import sqlite3

banco = sqlite3.connect('cadastro.db')

profissionais = banco.cursor()

#profissionais.execute("CREATE TABLE profissionais (nome text, bairro text, telefone integer, senha text)")

#profissionais.execute("INSERT INTO profissionais VALUES('Fulano','Grajaú','0000000','senha')")

#banco.commit()
profissionais.execute("SELECT * FROM profissionais")
print(profissionais.fetchall())