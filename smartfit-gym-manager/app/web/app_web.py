from datetime import date
from pathlib import Path

from flask import (
    Flask,
    flash,
    redirect,
    render_template,
    request,
    url_for,
)

from app.database.schema import criar_tabelas
from app.models.aluno import Aluno
from app.models.plano import Plano

from app.services.aluno_service import (
    cadastrar_aluno,
    listar_alunos,
)

from app.services.plano_service import (
    cadastrar_plano,
    listar_planos,
)

from app.services.relatorio_service import (
    relatorio_acessos,
    relatorio_financeiro,
    relatorio_geral,
)

from app.services.usuario_service import (
    criar_usuario_root,
)


RAIZ_PROJETO = Path(
    __file__
).resolve().parents[2]

CAMINHO_VERSION = (
    RAIZ_PROJETO
    / "VERSION"
)


def obter_versao():
    with open(
        CAMINHO_VERSION,
        "r",
        encoding="utf-8",
    ) as arquivo:
        return arquivo.read().strip()


def criar_app():
    app = Flask(
        __name__,
        template_folder="templates",
        static_folder="static",
    )

    app.config["SECRET_KEY"] = (
        "smartfit-gym-manager-dev"
    )

    criar_tabelas()
    criar_usuario_root()

    # ==========================================
    # DASHBOARD
    # ==========================================

    @app.route("/")
    def dashboard():
        geral = relatorio_geral()
        financeiro = relatorio_financeiro()
        acessos = relatorio_acessos()

        return render_template(
            "dashboard.html",
            versao=obter_versao(),
            geral=geral,
            financeiro=financeiro,
            acessos=acessos,
        )

    # ==========================================
    # ALUNOS
    # ==========================================

    @app.route(
        "/alunos",
        methods=[
            "GET",
            "POST",
        ],
    )
    def alunos():
        if request.method == "POST":
            nome = (
                request.form
                .get("nome", "")
                .strip()
            )

            cpf = (
                request.form
                .get("cpf", "")
                .strip()
            )

            data_nascimento_texto = (
                request.form
                .get(
                    "data_nascimento",
                    "",
                )
                .strip()
            )

            email = (
                request.form
                .get("email", "")
                .strip()
            )

            telefone = (
                request.form
                .get("telefone", "")
                .strip()
            )

            if not all(
                (
                    nome,
                    cpf,
                    data_nascimento_texto,
                    email,
                    telefone,
                )
            ):
                flash(
                    (
                        "Preencha todos os campos "
                        "antes de cadastrar o aluno."
                    ),
                    "erro",
                )

                return redirect(
                    url_for("alunos")
                )

            try:
                data_nascimento = (
                    date.fromisoformat(
                        data_nascimento_texto
                    )
                )

                aluno = Aluno(
                    nome=nome,
                    cpf=cpf,
                    data_nascimento=(
                        data_nascimento
                    ),
                    email=email,
                    telefone=telefone,
                    data_cadastro=date.today(),
                )

                aluno = cadastrar_aluno(
                    aluno
                )

                flash(
                    (
                        "Aluno cadastrado com "
                        "sucesso! "
                        f"ID: {aluno.id}"
                    ),
                    "sucesso",
                )

            except ValueError as erro:
                flash(
                    str(erro),
                    "erro",
                )

            except Exception as erro:
                flash(
                    (
                        "Não foi possível "
                        "cadastrar o aluno. "
                        f"{erro}"
                    ),
                    "erro",
                )

            return redirect(
                url_for("alunos")
            )

        alunos_cadastrados = (
            listar_alunos()
        )

        return render_template(
            "alunos.html",
            versao=obter_versao(),
            alunos=alunos_cadastrados,
        )

    # ==========================================
    # PLANOS
    # ==========================================

    @app.route(
        "/planos",
        methods=[
            "GET",
            "POST",
        ],
    )
    def planos():
        if request.method == "POST":
            nome = (
                request.form
                .get("nome", "")
                .strip()
            )

            valor_texto = (
                request.form
                .get("valor", "")
                .strip()
            )

            descricao = (
                request.form
                .get("descricao", "")
                .strip()
            )

            if not nome or not valor_texto:
                flash(
                    (
                        "Informe o nome e o "
                        "valor do plano."
                    ),
                    "erro",
                )

                return redirect(
                    url_for("planos")
                )

            try:
                valor = float(
                    valor_texto.replace(
                        ",",
                        ".",
                    )
                )

                if valor <= 0:
                    raise ValueError(
                        (
                            "O valor do plano deve "
                            "ser maior que zero."
                        )
                    )

                plano = Plano(
                    nome=nome,
                    valor=valor,
                    descricao=descricao,
                )

                plano = cadastrar_plano(
                    plano
                )

                flash(
                    (
                        "Plano cadastrado com "
                        "sucesso! "
                        f"ID: {plano.id}"
                    ),
                    "sucesso",
                )

            except ValueError as erro:
                flash(
                    str(erro),
                    "erro",
                )

            except Exception as erro:
                flash(
                    (
                        "Não foi possível "
                        "cadastrar o plano. "
                        f"{erro}"
                    ),
                    "erro",
                )

            return redirect(
                url_for("planos")
            )

        planos_cadastrados = (
            listar_planos()
        )

        return render_template(
            "planos.html",
            versao=obter_versao(),
            planos=planos_cadastrados,
        )

    return app


app = criar_app()


if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True,
    )