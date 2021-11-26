import sqlite3

banco = sqlite3.connect('cadastro.db')

usuarios = banco.cursor()

#usuarios.execute("CREATE TABLE IF NOT EXISTS usuarios (nome text, bairro text, telefone integer, senha text)")

#usuarios.execute("INSERT INTO usuarios VALUES('01','Fulano','Três Lagos','08000800','123Tatata')")


banco.commit()
usuarios.execute("SELECT * FROM usuarios")
print(usuarios.fetchall())

print("conectado ao banco de Dados")