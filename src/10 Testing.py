import sqlite3

conexao = sqlite3.connect("banco.db")# .cria ou abre o BD
cursor = conexao.cursor() #cria o cursor, (obj que executa comandos SQL)

cursor.execute("CREATE TABLE IF NOT EXISTS usuarios (nome TEXT, idade INTEGER)")# roda o comando

conexao.commit()
conexao.close()