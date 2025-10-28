from connection import conectar

def mostrar_todos_alunos():
    con = conectar()
    cur = con.cursor()
    cur.execute("SELECT * FROM Aluno;")
    alunos = cur.fetchall()
    con.close()
    
    if not alunos:
        return []
    return alunos

def top10_por_media():
    con = conectar()
    cur = con.cursor()
    cur.execute("""
        SELECT nome, nota1, nota2, (nota1 + nota2)/2 AS media
        FROM Aluno
        ORDER BY media DESC
        LIMIT 10;
    """)
    alunos = cur.fetchall()
    con.close()

    if not alunos:
        return []
    return alunos

def alunos_com_turma():
    con = conectar()
    cur = con.cursor()
    cur.execute("""
        SELECT Aluno.id, Aluno.nome, Aluno.nascimento, Aluno.nota1, Aluno.nota2, 
               Aluno.turma_id, Turma.nome, Turma.ano
        FROM Aluno
        LEFT JOIN Turma ON Aluno.turma_id = Turma.id;
    """)
    alunos = cur.fetchall()
    con.close()

    if not alunos:
        return []
    return alunos

def alunos_turma2():
    con = conectar()
    cur = con.cursor()
    cur.execute("""
        SELECT Aluno.id, Aluno.nome, Aluno.nascimento, Aluno.nota1, Aluno.nota2, 
               Aluno.turma_id, Turma.nome, Turma.ano
        FROM Aluno
        LEFT JOIN Turma ON Aluno.turma_id = Turma.id
        WHERE Aluno.turma_id = 2;
    """)
    alunos = cur.fetchall()
    con.close()

    if not alunos:
        return []
    return alunos
