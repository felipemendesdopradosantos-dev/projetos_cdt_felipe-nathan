import sqlite3
from datetime import datetime


def conectar():
    return sqlite3.connect("academia.db")


def criar_tabela_frequencia():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS frequencia (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            aluno_id INTEGER NOT NULL,
            data TEXT NOT NULL,
            horario TEXT NOT NULL,
            FOREIGN KEY (aluno_id) REFERENCES alunos(id)
        )
    """)

    conexao.commit()
    conexao.close()


def registrar_acesso(aluno_id):
    agora = datetime.now()

    data = agora.strftime("%d/%m/%Y")
    horario = agora.strftime("%H:%M:%S")

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        INSERT INTO frequencia (aluno_id, data, horario)
        VALUES (?, ?, ?)
    """, (aluno_id, data, horario))

    conexao.commit()
    conexao.close()


def listar_frequencia():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT
            frequencia.id,
            alunos.id,
            alunos.nome,
            frequencia.data,
            frequencia.horario
        FROM frequencia
        INNER JOIN alunos
        ON frequencia.aluno_id = alunos.id
        ORDER BY frequencia.id DESC
    """)

    registros = cursor.fetchall()

    conexao.close()

    return registros


criar_tabela_frequencia()