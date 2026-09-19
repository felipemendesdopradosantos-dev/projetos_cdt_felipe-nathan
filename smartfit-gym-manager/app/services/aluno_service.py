import sqlite3
from datetime import date

from app.database.connection import obter_conexao
from app.models.aluno import Aluno


def cadastrar_aluno(aluno: Aluno) -> Aluno:
    conexao = obter_conexao()

    try:
        cursor = conexao.execute(
            """
            INSERT INTO alunos (
                nome,
                cpf,
                data_nascimento,
                email,
                telefone,
                data_cadastro,
                status
            )
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (
                aluno.nome,
                aluno.cpf,
                aluno.data_nascimento.isoformat(),
                aluno.email,
                aluno.telefone,
                aluno.data_cadastro.isoformat(),
                aluno.status,
            ),
        )

        conexao.commit()

        aluno.id = cursor.lastrowid

        return aluno

    except sqlite3.IntegrityError as erro:
        raise ValueError(
            "Não foi possível cadastrar o aluno. "
            "Verifique se CPF ou e-mail já estão cadastrados."
        ) from erro

    finally:
        conexao.close()


def listar_alunos() -> list[Aluno]:
    conexao = obter_conexao()

    try:
        linhas = conexao.execute(
            """
            SELECT
                id,
                nome,
                cpf,
                data_nascimento,
                email,
                telefone,
                data_cadastro,
                status
            FROM alunos
            ORDER BY nome
            """
        ).fetchall()

        return [_linha_para_aluno(linha) for linha in linhas]

    finally:
        conexao.close()


def buscar_aluno_por_id(aluno_id: int) -> Aluno | None:
    conexao = obter_conexao()

    try:
        linha = conexao.execute(
            """
            SELECT
                id,
                nome,
                cpf,
                data_nascimento,
                email,
                telefone,
                data_cadastro,
                status
            FROM alunos
            WHERE id = ?
            """,
            (aluno_id,),
        ).fetchone()

        if linha is None:
            return None

        return _linha_para_aluno(linha)

    finally:
        conexao.close()


def buscar_aluno_por_cpf(cpf: str) -> Aluno | None:
    conexao = obter_conexao()

    try:
        linha = conexao.execute(
            """
            SELECT
                id,
                nome,
                cpf,
                data_nascimento,
                email,
                telefone,
                data_cadastro,
                status
            FROM alunos
            WHERE cpf = ?
            """,
            (cpf,),
        ).fetchone()

        if linha is None:
            return None

        return _linha_para_aluno(linha)

    finally:
        conexao.close()


def _linha_para_aluno(linha) -> Aluno:
    return Aluno(
        id=linha["id"],
        nome=linha["nome"],
        cpf=linha["cpf"],
        data_nascimento=date.fromisoformat(linha["data_nascimento"]),
        email=linha["email"],
        telefone=linha["telefone"],
        data_cadastro=date.fromisoformat(linha["data_cadastro"]),
        status=linha["status"],
    )