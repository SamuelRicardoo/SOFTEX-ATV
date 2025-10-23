import sqlite3

DB_NAME = "escola_v2.db"

def conectar():
    return sqlite3.connect(DB_NAME)

def criar_tabela():
    con = conectar()
    cur = con.cursor()

    # Tabela Aluno
    cur.execute("""
        CREATE TABLE IF NOT EXISTS Aluno (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            nascimento DATE,
            nota1 REAL,
            nota2 REAL,
            turma_id INTEGER
        );
    """)

    # Tabela Curso
    cur.execute("""
        CREATE TABLE IF NOT EXISTS Curso (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            mensalidade REAL
        );
    """)

    # Tabela Turma
    cur.execute("""
        CREATE TABLE IF NOT EXISTS Turma (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            ano INTEGER
        );
    """)

    con.commit()
    con.close()
