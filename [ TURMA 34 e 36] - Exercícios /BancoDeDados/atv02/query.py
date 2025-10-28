from connection import conectar

def total_alunos():
    con = conectar()
    cur = con.cursor()
    cur.execute("SELECT COUNT(*) FROM Aluno;")
    resultado = cur.fetchone()[0]
    con.close()
    return resultado

def menor_mensalidade():
    con = conectar()
    cur = con.cursor()
    cur.execute("SELECT MIN(mensalidade) FROM Curso;")
    resultado = cur.fetchone()[0]
    con.close()
    return resultado

def maior_nota1():
    con = conectar()
    cur = con.cursor()
    cur.execute("SELECT MAX(nota1) FROM Aluno;")
    resultado = cur.fetchone()[0]
    con.close()
    return resultado

def total_mensalidades():
    con = conectar()
    cur = con.cursor()
    cur.execute("SELECT SUM(mensalidade) FROM Curso;")
    resultado = cur.fetchone()[0]
    con.close()
    return resultado

def media_nota2():
    con = conectar()
    cur = con.cursor()
    cur.execute("SELECT AVG(nota2) FROM Aluno;")
    resultado = cur.fetchone()[0]
    con.close()
    return resultado
