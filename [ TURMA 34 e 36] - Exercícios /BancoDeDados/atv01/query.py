from connection import conectar

def mostrar_todos_alunos():
    con = conectar()
    cur = con.cursor()
    cur.execute("SELECT * FROM Aluno;")
    alunos = cur.fetchall()
    con.close()

    if not alunos:
        return []
    else:
        return alunos

def exibir_nome_e_nota1():
    con = conectar()
    cur = con.cursor()
    cur.execute("SELECT nome, nota1 FROM Aluno;")
    alunos = cur.fetchall()
    con.close()
    
    if not alunos:
        return []
    else:
        return alunos

def alunos_com_nota2_maior_que_8():
    con = conectar()
    cur = con.cursor()
    cur.execute("SELECT * FROM Aluno WHERE nota2 > 8;")
    alunos = cur.fetchall()
    con.close()
    
    if not alunos:
        return []
    else:
        return alunos

def alunos_nascidos_apos_2000():
    con = conectar()
    cur = con.cursor()
    cur.execute("SELECT * FROM Aluno WHERE nascimento > '2000-12-31';")
    alunos = cur.fetchall()
    con.close()
    
    if not alunos:
        return []
    else:
        return alunos

def cursos_com_mensalidade_maior_600():
    con = conectar()
    cur = con.cursor()
    cur.execute("SELECT nome, mensalidade FROM Curso WHERE mensalidade > 600;")
    alunos = cur.fetchall()
    con.close()
    
    if not alunos:
        return []
    else:
        return alunos
    
def turmas_ordenadas_por_ano():
    con = conectar()
    cur = con.cursor()
    cur.execute("SELECT nome, ano FROM Turma ORDER BY ano ASC;")
    alunos = cur.fetchall()
    con.close()

    if not alunos:
        return []
    else:
        return alunos

def quantidade_turmas_por_ano():
    con = conectar()
    cur = con.cursor()
    cur.execute("SELECT ano, COUNT(*) FROM Turma GROUP BY ano;")
    alunos = cur.fetchall()
    con.close()

    if not alunos:
        return []
    else:
        return alunos

def media_nota1_por_turma():
    con = conectar()
    cur = con.cursor()
    cur.execute("SELECT turma_id, AVG(nota1) FROM Aluno GROUP BY turma_id;")
    alunos = cur.fetchall()
    con.close()

    if not alunos:
        return []
    else:
        return alunos

def anos_com_mais_de_duas_turmas():
    con = conectar()
    cur = con.cursor()
    cur.execute("SELECT ano, COUNT(*) FROM Turma GROUP BY ano HAVING COUNT(*) > 2;")
    alunos = cur.fetchall()
    con.close()

    if not alunos:
        return []
    else:
        return alunos

def cursos_ordenados_por_mensalidade():
    con = conectar()
    cur = con.cursor()
    cur.execute("SELECT nome, mensalidade FROM Curso ORDER BY mensalidade DESC;")
    alunos = cur.fetchall()
    con.close()
    
    if not alunos:
        return []
    else:
        return alunos
    

def mocar_dados():
    con = conectar()
    cur = con.cursor()

    cur.executemany("""
        INSERT INTO Curso (nome, mensalidade) VALUES (?, ?)
    """, [
        ('Engenharia de Software', 850.00),
        ('Administração', 620.00),
        ('Design Gráfico', 580.00),
        ('Ciência de Dados', 900.00),
        ('Marketing Digital', 610.00),
        ('Psicologia', 750.00),
        ('Engenharia Civil', 980.00),
        ('Jornalismo', 590.00),
        ('Sistemas de Informação', 820.00),
        ('Recursos Humanos', 605.00)
    ])

    cur.executemany("""
        INSERT INTO Turma (nome, ano) VALUES (?, ?)
    """, [
        ('Turma A', 2022),
        ('Turma B', 2023),
        ('Turma C', 2023),
        ('Turma D', 2024),
        ('Turma E', 2024),
        ('Turma F', 2024),
        ('Turma G', 2025),
        ('Turma H', 2025),
        ('Turma I', 2025)
    ])

    cur.executemany("""
        INSERT INTO Aluno (nome, nascimento, nota1, nota2, turma_id) VALUES (?, ?, ?, ?, ?)
    """, [
        ('Ana Souza', '2002-05-14', 8.5, 9.0, 1),
        ('Bruno Lima', '1999-11-22', 7.0, 6.5, 2),
        ('Carla Mendes', '2001-03-30', 9.2, 8.7, 1),
        ('Diego Rocha', '2003-07-19', 6.8, 7.5, 3),
        ('Eduarda Silva', '2000-12-01', 8.0, 9.5, 2),
        ('Felipe Torres', '2004-01-10', 7.5, 8.2, 3),
        ('Gabriela Costa', '2005-08-22', 9.0, 9.3, 4),
        ('Henrique Martins', '1998-04-17', 6.5, 7.0, 1),
        ('Isabela Freitas', '2002-10-05', 8.8, 8.9, 5),
        ('João Pedro', '2001-06-12', 7.2, 6.8, 2),
        ('Larissa Cunha', '2003-09-30', 9.5, 9.7, 6),
        ('Matheus Andrade', '2000-02-25', 6.9, 7.4, 4),
        ('Natalia Ribeiro', '2005-11-03', 8.6, 9.1, 5),
        ('Otávio Fernandes', '2003-03-15', 7.8, 8.0, 6),
        ('Paula Nogueira', '2004-07-28', 9.3, 9.6, 7),
        ('Ricardo Alves', '1997-12-20', 6.2, 6.9, 1),
        ('Sofia Martins', '2002-02-11', 8.7, 9.2, 8),
        ('Thiago Costa', '2001-09-09', 7.4, 7.8, 9)
    ])

    con.commit()
    con.close()
    print("Dados mock inseridos com sucesso!")   
    
    