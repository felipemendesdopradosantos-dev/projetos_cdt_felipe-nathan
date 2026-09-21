import json
from datetime import datetime
from pathlib import Path

from app.database.connection import obter_conexao


RAIZ_PROJETO = Path(__file__).resolve().parents[2]

PASTA_EXPORTS = (
    RAIZ_PROJETO
    / "data"
    / "exports"
)

CAMINHO_VERSION = (
    RAIZ_PROJETO
    / "VERSION"
)


TABELAS_EXPORTADAS = (
    "alunos",
    "planos",
    "assinaturas",
    "pagamentos",
    "acessos",
    "treinos",
    "exercicios",
    "treino_exercicios",
)


def obter_versao() -> str:
    with open(
        CAMINHO_VERSION,
        "r",
        encoding="utf-8",
    ) as arquivo:
        return arquivo.read().strip()


def buscar_dados_tabela(
    nome_tabela: str,
) -> list[dict]:
    if nome_tabela not in TABELAS_EXPORTADAS:
        raise ValueError(
            f"Tabela não permitida: {nome_tabela}"
        )

    conexao = obter_conexao()

    try:
        linhas = conexao.execute(
            f"SELECT * FROM {nome_tabela}"
        ).fetchall()

        return [
            dict(linha)
            for linha in linhas
        ]

    finally:
        conexao.close()


def exportar_banco_json() -> Path:
    PASTA_EXPORTS.mkdir(
        parents=True,
        exist_ok=True,
    )

    momento_exportacao = datetime.now()

    dados = {
        "sistema": "SmartFit Gym Manager",
        "versao": obter_versao(),
        "data_exportacao": (
            momento_exportacao.isoformat(
                timespec="seconds"
            )
        ),
        "dados": {},
    }

    for tabela in TABELAS_EXPORTADAS:
        dados["dados"][tabela] = (
            buscar_dados_tabela(tabela)
        )

    nome_arquivo = (
        "academia_"
        f"{momento_exportacao.strftime('%Y%m%d_%H%M%S')}"
        ".json"
    )

    caminho_arquivo = (
        PASTA_EXPORTS
        / nome_arquivo
    )

    with open(
        caminho_arquivo,
        "w",
        encoding="utf-8",
    ) as arquivo:
        json.dump(
            dados,
            arquivo,
            ensure_ascii=False,
            indent=4,
        )

    return caminho_arquivo