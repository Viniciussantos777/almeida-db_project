import sqlite3

def connect():
    conexao = sqlite3.connect('almeida_db_project.db')
    cursor = conexao.cursor()
    return conexao,cursor