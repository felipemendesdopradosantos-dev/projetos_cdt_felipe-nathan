from pathlib import Path

from app.database.schema import criar_tabelas


def obter_versao():
    caminho_versao = Path(__file__).parent / "VERSION"

    with open(caminho_versao, "r", encoding="utf-8") as arquivo:
        return arquivo.read().strip()


def main():
    versao = obter_versao()

    print("SmartFit Gym Manager")
    print(f"Versão {versao}")
    print()

    criar_tabelas()

    print("Banco de dados inicializado com sucesso.")
    print("Sistema em desenvolvimento.")


if __name__ == "__main__":
    main()