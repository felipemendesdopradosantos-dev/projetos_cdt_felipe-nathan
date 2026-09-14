import sqlite3


def conectar():
    return sqlite3.connect("academia.db")


def criar_tabela_alunos():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS alunos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            idade INTEGER NOT NULL,
            telefone TEXT NOT NULL,
            email TEXT NOT NULL,
            plano TEXT NOT NULL,
            valor_plano REAL NOT NULL,
            status TEXT NOT NULL DEFAULT 'Ativo'
        )
    """)

    conexao.commit()
    conexao.close()


def cadastrar_aluno(nome, idade, telefone, email, plano, valor_plano):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        INSERT INTO alunos
        (nome, idade, telefone, email, plano, valor_plano, status)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        nome,
        idade,
        telefone,
        email,
        plano,
        valor_plano,
        "Ativo"
    ))

    conexao.commit()
    conexao.close()


def listar_alunos():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM alunos")
    alunos = cursor.fetchall()

    conexao.close()

    return alunos


def buscar_aluno(id_aluno):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        "SELECT * FROM alunos WHERE id = ?",
        (id_aluno,)
    )

    aluno = cursor.fetchone()

    conexao.close()

    return aluno

def editar_aluno(id_aluno, nome, idade, telefone, email, plano, valor_plano):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        UPDATE alunos
        SET nome = ?,
            idade = ?,
            telefone = ?,
            email = ?,
            plano = ?,
            valor_plano = ?
        WHERE id = ?
    """, (
        nome,
        idade,
        telefone,
        email,
        plano,
        valor_plano,
        id_aluno
    ))

    conexao.commit()
    conexao.close()


def excluir_aluno(id_aluno):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        "DELETE FROM alunos WHERE id = ?",
        (id_aluno,)
    )

    conexao.commit()
    conexao.close()

criar_tabela_alunos()