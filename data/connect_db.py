import sqlite3

def connect_db():
    conexao = sqlite3.connect('almeida_db_project.db')
    cursor = conexao.cursor()
    return conexao, cursor