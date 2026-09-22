# SmartFit Gym Manager

Sistema de gerenciamento de academia desenvolvido em Python como projeto final de programação.

**Versão atual: `0.6.0`**

> Projeto acadêmico independente, sem vínculo oficial com a Smart Fit.

---

## Sobre o projeto

O **SmartFit Gym Manager** é uma aplicação desenvolvida para automatizar processos comuns de gerenciamento de uma academia.

O sistema reúne funcionalidades relacionadas a:

- alunos;
- planos;
- assinaturas;
- pagamentos;
- inadimplência;
- controle de acesso;
- exercícios;
- fichas de treino;
- relatórios;
- geração de dados fictícios;
- exportação de dados;
- acesso Web;
- interface responsiva;
- acesso por QR Code.

A arquitetura foi estruturada para permitir que diferentes interfaces utilizem as mesmas regras de negócio e o mesmo banco de dados.

```text
                 CLI
                  │
                  │
GUI ───────── Services ───────── WEB
                  │
                  ↓
               SQLite
```

Atualmente o sistema possui três interfaces funcionais:

- CLI;
- GUI com Tkinter;
- aplicação Web com Flask.

---

# Objetivos

O projeto tem como objetivo desenvolver uma aplicação capaz de:

- cadastrar e consultar alunos;
- cadastrar e consultar planos;
- criar assinaturas;
- gerar cobranças;
- registrar pagamentos;
- identificar automaticamente inadimplência;
- autorizar ou negar acesso à academia;
- armazenar histórico de acessos;
- cadastrar exercícios;
- criar fichas de treino;
- associar exercícios aos treinos;
- gerar dados fictícios com Faker;
- gerar relatórios administrativos;
- exportar o banco de dados para JSON;
- proteger a exportação através de autenticação administrativa;
- disponibilizar interfaces CLI, GUI e Web;
- funcionar em dispositivos móveis;
- disponibilizar acesso através de QR Code;
- disponibilizar uma versão executável;
- disponibilizar a aplicação Web através de um serviço de hospedagem.

---

# Tecnologias

## Implementadas

- Python
- SQLite
- JSON
- Faker
- Tkinter
- Pytest
- Flask
- HTML
- CSS
- QR Code
- Pillow

## Próximas etapas

- PyInstaller
- Render

---

# Arquitetura

O projeto utiliza separação de responsabilidades entre diferentes camadas.

```text
Interfaces
    │
    ↓
Services
    │
    ↓
Models
    │
    ↓
SQLite
```

## Interfaces

Existem três interfaces funcionais:

```text
CLI
GUI
WEB
```

Todas reutilizam a mesma camada de Services.

## Models

Representam as principais entidades do sistema:

- Aluno
- Plano
- Assinatura
- Pagamento
- Acesso
- Exercício
- Treino
- Usuário

## Services

Contêm as regras de negócio e operações realizadas pelo sistema.

Entre suas responsabilidades estão:

- gerenciamento de alunos;
- gerenciamento de planos;
- gerenciamento de assinaturas;
- gerenciamento de pagamentos;
- controle de inadimplência;
- controle de acesso;
- gerenciamento de exercícios;
- gerenciamento de treinos;
- geração de relatórios;
- geração de dados fictícios;
- autenticação administrativa;
- exportação JSON.

## Database

Responsável pela conexão e criação da estrutura do banco SQLite.

---

# Estrutura do projeto

```text
smartfit-gym-manager/
│
├── app/
│   ├── __init__.py
│   │
│   ├── cli/
│   │   ├── __init__.py
│   │   └── menu.py
│   │
│   ├── database/
│   │   ├── __init__.py
│   │   ├── connection.py
│   │   └── schema.py
│   │
│   ├── gui/
│   │   ├── __init__.py
│   │   ├── janela_principal.py
│   │   ├── tela_acesso.py
│   │   ├── tela_alunos.py
│   │   ├── tela_assinaturas.py
│   │   ├── tela_exportacao.py
│   │   ├── tela_pagamentos.py
│   │   ├── tela_planos.py
│   │   ├── tela_relatorios.py
│   │   └── tela_treinos.py
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   ├── acesso.py
│   │   ├── aluno.py
│   │   ├── assinatura.py
│   │   ├── exercicio.py
│   │   ├── pagamento.py
│   │   ├── plano.py
│   │   ├── treino.py
│   │   └── usuario.py
│   │
│   ├── services/
│   │   ├── __init__.py
│   │   ├── acesso_service.py
│   │   ├── aluno_service.py
│   │   ├── assinatura_service.py
│   │   ├── exercicio_service.py
│   │   ├── export_service.py
│   │   ├── faker_service.py
│   │   ├── pagamento_service.py
│   │   ├── plano_service.py
│   │   ├── relatorio_service.py
│   │   ├── treino_service.py
│   │   └── usuario_service.py
│   │
│   └── web/
│       ├── __init__.py
│       ├── app_web.py
│       │
│       ├── static/
│       │   └── css/
│       │       └── style.css
│       │
│       └── templates/
│           ├── acesso.html
│           ├── alunos.html
│           ├── assinaturas.html
│           ├── base.html
│           ├── dashboard.html
│           ├── exportacao.html
│           ├── pagamentos.html
│           ├── planos.html
│           ├── qr_code.html
│           └── relatorios.html
│
├── data/
│   ├── academia.db
│   └── exports/
│
├── docs/
│   ├── papeis_projeto.md
│   └── requisitos.md
│
├── tests/
│   ├── conftest.py
│   ├── test_acesso_service.py
│   ├── test_aluno_service.py
│   ├── test_database.py
│   ├── test_pagamento_service.py
│   ├── test_plano_service.py
│   ├── test_relatorio_service.py
│   ├── test_usuario_service.py
│   └── test_web.py
│
├── .gitignore
├── CHANGELOG.md
├── LICENSE
├── main.py
├── README.md
├── requirements.txt
└── VERSION
```

---

# Banco de dados

O sistema utiliza **SQLite** como banco de dados local.

Arquivo principal:

```text
data/academia.db
```

O banco é criado automaticamente durante a inicialização da aplicação.

## Tabelas

Existem nove tabelas principais:

```text
alunos
planos
assinaturas
pagamentos
acessos
treinos
exercicios
treino_exercicios
usuarios
```

---

# Alunos

O sistema permite:

- cadastrar alunos;
- listar alunos;
- buscar aluno por ID;
- buscar aluno por CPF;
- controlar status;
- impedir CPF duplicado;
- impedir e-mail duplicado.

O gerenciamento de alunos está disponível pela:

```text
CLI
GUI
WEB
```

---

# Planos

O sistema permite:

- cadastrar planos;
- listar planos;
- buscar plano por ID;
- buscar plano por nome;
- controlar status;
- impedir nomes duplicados.

A validação de nomes duplicados ignora:

- diferenças entre letras maiúsculas e minúsculas;
- espaços no início e no final.

Exemplos considerados equivalentes:

```text
Plano Web
plano web
PLANO WEB
 Plano Web
Plano Web 
```

Além da validação no Service, o banco possui proteção através de:

```sql
LOWER(TRIM(nome))
```

---

# Assinaturas

O sistema permite:

- associar aluno a um plano;
- listar assinaturas;
- identificar assinatura ativa;
- impedir múltiplas assinaturas ativas para o mesmo aluno.

Fluxo:

```text
Aluno
  ↓
Plano
  ↓
Assinatura
```

A criação de assinaturas está disponível nas interfaces CLI, GUI e Web.

---

# Pagamentos

O módulo financeiro permite:

- gerar cobranças;
- definir vencimentos;
- registrar pagamentos;
- registrar forma de pagamento;
- listar pagamentos;
- identificar pagamentos pendentes;
- identificar pagamentos atrasados;
- atualizar automaticamente cobranças vencidas;
- identificar inadimplência.

Fluxo:

```text
Assinatura
    ↓
Cobrança
    ↓
Pagamento
    ↓
Pago / Pendente / Atrasado
```

A aplicação Web permite gerar cobranças, registrar pagamentos e consultar o histórico financeiro.

---

# Controle de acesso

O acesso do aluno é avaliado automaticamente.

```text
Aluno tenta acessar
        │
        ↓
Aluno existe?
        │
        ↓
Aluno está ativo?
        │
        ↓
Possui assinatura ativa?
        │
        ↓
Possui pagamento atrasado?
        │
        ↓
AUTORIZADO / NEGADO
        │
        ↓
Registro no histórico
```

O sistema registra tanto acessos autorizados quanto negados.

Exemplos:

```text
ACESSO AUTORIZADO
```

```text
ACESSO NEGADO
Motivo: Aluno sem assinatura ativa.
```

```text
ACESSO NEGADO
Motivo: Pagamento em atraso.
```

O controle de acesso está disponível pela CLI, GUI e Web.

---

# Exercícios e treinos

O sistema possui gerenciamento de exercícios e fichas de treino.

É possível:

- cadastrar exercícios;
- informar grupo muscular;
- adicionar descrição;
- criar treino para aluno;
- informar objetivo;
- associar exercícios;
- definir séries;
- definir repetições;
- definir carga;
- definir descanso;
- definir ordem;
- visualizar ficha completa.

Exemplo:

```text
Treino A
Objetivo: Hipertrofia

1 - Supino Reto
Grupo: Peitoral
Séries: 4
Repetições: 8-12
Carga: 50 kg
Descanso: 90 segundos
```

---

# Relatórios

O sistema possui quatro categorias principais.

## Relatório geral

Apresenta:

- total de alunos;
- alunos ativos;
- assinaturas ativas;
- planos ativos.

## Relatório financeiro

Apresenta:

- total recebido;
- valor pendente;
- valor atrasado;
- quantidade de pagamentos realizados;
- quantidade de pagamentos pendentes;
- quantidade de pagamentos atrasados.

## Relatório de acessos

Apresenta:

- total de acessos;
- acessos autorizados;
- acessos negados;
- ranking de frequência.

## Relatório de planos

Apresenta:

- nome do plano;
- valor mensal;
- quantidade de assinaturas ativas.

Os mesmos Services de relatório são utilizados pela CLI, GUI e Web.

---

# Faker

O projeto utiliza **Faker** para geração automática de dados fictícios.

Podem ser gerados:

- alunos;
- assinaturas;
- pagamentos;
- acessos.

Os dados são armazenados no mesmo SQLite utilizado pelo restante da aplicação.

---

# Exportação JSON

O banco pode ser exportado para JSON.

Arquivos são armazenados em:

```text
data/exports/
```

Exemplo:

```text
academia_20260921_220000.json
```

A exportação contém:

```text
alunos
planos
assinaturas
pagamentos
acessos
treinos
exercicios
treino_exercicios
```

A tabela:

```text
usuarios
```

não é exportada.

A exportação está disponível pela:

```text
CLI
GUI
WEB
```

Na Web, além de salvar a cópia local, o arquivo é enviado para download pelo navegador.

---

# Usuário administrador

A exportação JSON é protegida por autenticação.

Credenciais acadêmicas:

```text
Usuário: root master
Senha: root
```

A senha não é armazenada diretamente em texto puro no banco.

O sistema armazena um hash utilizado para validação.

Na CLI e na GUI a senha é mascarada.

Na Web é utilizado:

```html
<input type="password">
```

> As credenciais padrão existem para fins acadêmicos. Uma aplicação real deve utilizar credenciais configuráveis e mecanismos específicos para armazenamento seguro de senhas.

---

# Interface CLI

A CLI representa a primeira interface funcional do projeto.

## Executar

```bash
py main.py
```

## Menu principal

```text
1  - Cadastrar aluno
2  - Listar alunos

3  - Cadastrar plano
4  - Listar planos

5  - Criar assinatura
6  - Listar assinaturas

7  - Gerar cobrança
8  - Listar pagamentos
9  - Registrar pagamento

10 - Registrar acesso
11 - Histórico de acessos

12 - Cadastrar exercício
13 - Listar exercícios

14 - Criar treino
15 - Listar treinos de um aluno
16 - Adicionar exercício ao treino
17 - Visualizar ficha de treino

18 - Exportar banco para JSON
19 - Gerar dados fictícios com Faker
20 - Relatórios

0  - Sair
```

---

# Interface GUI

A segunda interface utiliza **Tkinter**.

## Executar

```bash
py -m app.gui.janela_principal
```

A GUI possui:

```text
Dashboard
Alunos
Planos
Assinaturas
Pagamentos
Controle de Acesso
Treinos
Relatórios
Exportação JSON
```

A GUI utiliza os mesmos Services e o mesmo SQLite da CLI.

---

# Interface Web

A terceira interface utiliza:

```text
Flask
HTML
CSS
```

## Executar

```bash
py -m app.web.app_web
```

O servidor utiliza:

```python
host="0.0.0.0"
port=5000
```

Isso permite acesso através do próprio computador e de outros dispositivos na mesma rede local.

No computador:

```text
http://127.0.0.1:5000
```

Na rede local:

```text
http://IP_DO_COMPUTADOR:5000
```

---

# Funcionalidades Web

A versão Web possui:

- Dashboard;
- Alunos;
- Planos;
- Assinaturas;
- Pagamentos;
- Controle de Acesso;
- Relatórios;
- Exportação JSON;
- QR Code.

---

# Dashboard Web

Apresenta:

- total de alunos;
- assinaturas ativas;
- total recebido;
- quantidade de acessos;
- alunos ativos;
- planos ativos;
- pagamentos pendentes;
- pagamentos atrasados;
- acessos autorizados;
- acessos negados.

---

# Alunos Web

Rota:

```text
/alunos
```

Permite cadastrar e consultar alunos diretamente pelo navegador.

---

# Planos Web

Rota:

```text
/planos
```

Permite cadastrar e consultar planos.

As regras de duplicidade do `plano_service.py` também são aplicadas na Web.

---

# Assinaturas Web

Rota:

```text
/assinaturas
```

Permite:

- selecionar aluno;
- selecionar plano;
- definir data de início;
- definir data final;
- criar assinatura;
- visualizar assinaturas cadastradas.

---

# Pagamentos Web

Rota:

```text
/pagamentos
```

Permite:

- gerar cobranças;
- selecionar assinatura;
- definir vencimento;
- registrar pagamento;
- selecionar forma de pagamento;
- consultar histórico financeiro.

---

# Controle de Acesso Web

Rota:

```text
/acesso
```

Permite verificar a entrada de um aluno.

O sistema avalia:

```text
status do aluno
assinatura
inadimplência
```

e retorna:

```text
AUTORIZADO
```

ou:

```text
NEGADO
```

Todas as tentativas são registradas.

---

# Relatórios Web

Rota:

```text
/relatorios
```

Disponibiliza:

```text
Geral
Financeiro
Acessos
Ranking de frequência
Planos
```

---

# Exportação JSON Web

Rota:

```text
/exportacao
```

Exige autenticação administrativa antes da exportação.

Após autenticação correta:

```text
SQLite
   ↓
export_service.py
   ↓
JSON
   ↓
data/exports/
   +
download pelo navegador
```

---

# Interface responsiva

A aplicação Web possui layout responsivo.

Foi realizada validação específica na resolução:

```text
320 x 800 px
```

Em telas menores:

- menu lateral passa para o topo;
- navegação é organizada em duas colunas;
- cards passam para uma coluna;
- formulários passam para uma coluna;
- textos podem quebrar linha;
- componentes respeitam a largura disponível;
- tabelas utilizam rolagem horizontal própria.

A interface foi validada através das ferramentas de dispositivo do navegador e também em dispositivo móvel real.

---

# QR Code

A aplicação possui uma página dedicada ao QR Code.

Rota:

```text
/qr
```

Imagem:

```text
/qr/imagem
```

O endereço local do computador é identificado automaticamente.

Fluxo:

```text
Flask
  ↓
IP local
  ↓
URL da aplicação
  ↓
QR Code
  ↓
Celular
  ↓
Dashboard
```

O celular deve estar conectado à mesma rede local do computador durante a execução local.

O QR Code foi validado com sucesso em dispositivo móvel real.

---

# Instalação

## 1. Clonar o repositório

```bash
git clone URL_DO_REPOSITORIO
```

## 2. Entrar no projeto

```bash
cd smartfit-gym-manager
```

## 3. Instalar dependências

```bash
py -m pip install -r requirements.txt
```

## 4. Executar CLI

```bash
py main.py
```

## 5. Executar GUI

```bash
py -m app.gui.janela_principal
```

## 6. Executar Web

```bash
py -m app.web.app_web
```

---

# Dependências

As dependências são registradas no:

```text
requirements.txt
```

Principais dependências externas:

```text
Flask
Faker
qrcode[pil]
pytest
pyinstaller
```

Bibliotecas como estas fazem parte do Python ou da instalação padrão:

```text
sqlite3
json
hashlib
datetime
pathlib
socket
tkinter
```

---

# Testes automatizados

O projeto utiliza **Pytest**.

## Executar

```bash
py -m pytest -v
```

Resultado atual:

```text
35 passed
```

Os testes utilizam bancos SQLite temporários para não alterar:

```text
data/academia.db
```

---

# Testes da camada Web

A versão `0.6.0` adicionou testes específicos da aplicação Flask.

Foram adicionados testes para:

- abertura das principais páginas;
- geração da imagem do QR Code;
- cadastro de aluno pela Web;
- bloqueio de plano duplicado pela Web;
- fluxo principal integrado da aplicação.

O teste de integração executa:

```text
Aluno
 ↓
Plano
 ↓
Assinatura
 ↓
Cobrança
 ↓
Pagamento
 ↓
Controle de acesso
 ↓
AUTORIZADO
```

---

# Cenários de testes

A suíte inclui cenários relacionados a:

- criação das tabelas;
- autenticação;
- cadastro de alunos;
- CPF duplicado;
- e-mail duplicado;
- planos;
- planos duplicados;
- normalização de nomes;
- pagamentos;
- inadimplência;
- acessos;
- relatórios;
- rotas Flask;
- QR Code;
- integração Web.

Resultado:

```text
35 passed
```

---

# Versionamento

O projeto utiliza **Versionamento Semântico**:

```text
MAJOR.MINOR.PATCH
```

## PATCH

Correções de bugs.

Exemplo:

```text
0.5.0 → 0.5.1
```

## MINOR

Novas funcionalidades compatíveis.

Exemplo:

```text
0.5.1 → 0.6.0
```

A versão `0.6.0` foi criada após a conclusão da aplicação Web funcional.

## MAJOR

Mudanças estruturais importantes ou lançamento da versão estável.

Exemplo:

```text
0.9.0 → 1.0.0
```

A versão está registrada em:

```text
VERSION
```

O histórico está em:

```text
CHANGELOG.md
```

---

# Versão atual

```text
0.6.0
```

A versão `0.6.0` consolida a terceira interface funcional do sistema.

Principais recursos:

- CLI funcional;
- GUI funcional;
- Web funcional;
- banco SQLite compartilhado;
- gerenciamento de alunos;
- gerenciamento de planos;
- assinaturas;
- pagamentos;
- inadimplência;
- controle de acesso;
- treinos;
- exercícios;
- relatórios;
- Faker;
- exportação JSON;
- autenticação administrativa;
- interface responsiva;
- mobile `320 x 800`;
- acesso pela rede local;
- QR Code;
- 35 testes automatizados aprovados.

---

# Papéis do projeto

Durante o desenvolvimento são considerados:

```text
PO - Product Owner
QA - Quality Assurance
UX - User Experience
Tech Lead / Desenvolvedor
IA - Inteligência Artificial
```

## Product Owner

Responsável por:

- definição do objetivo;
- funcionalidades;
- escopo;
- priorização;
- organização das versões.

## QA

Responsável por:

- testes manuais;
- testes automatizados;
- validação de regras;
- identificação de erros;
- testes de regressão;
- validação das interfaces.

## UX

Responsável por:

- organização visual;
- navegação;
- formulários;
- mensagens;
- responsividade;
- experiência de uso.

## Tech Lead / Desenvolvedor

Responsável por:

- arquitetura;
- models;
- services;
- banco;
- interfaces;
- integração;
- versionamento;
- desenvolvimento.

## Inteligência Artificial

Utilizada como ferramenta de apoio para:

- planejamento;
- arquitetura;
- desenvolvimento;
- revisão;
- testes;
- documentação;
- explicação de conceitos.

As decisões e validações finais permanecem sob responsabilidade do desenvolvedor.

---

# Documentação

Arquivos complementares:

```text
docs/
├── requisitos.md
└── papeis_projeto.md
```

---

# Executável

Está prevista a criação de uma versão executável utilizando **PyInstaller**.

Objetivo:

```text
SmartFitGymManager.exe
```

O executável deverá abrir a interface gráfica sem exigir comandos no terminal.

---

# Publicação Web

A próxima etapa é disponibilizar a aplicação em um ambiente Web.

A opção planejada é:

```text
Render
```

Fluxo esperado:

```text
GitHub
   ↓
Render
   ↓
URL pública
   ↓
Aplicação Flask
   ↓
QR Code
   ↓
Celular
```

---

# Roadmap

## Concluído

- [x] Estrutura modular
- [x] SQLite
- [x] Models
- [x] Services
- [x] CLI
- [x] GUI Tkinter
- [x] Dashboard GUI
- [x] Alunos
- [x] Planos
- [x] Assinaturas
- [x] Pagamentos
- [x] Inadimplência
- [x] Controle de acesso
- [x] Exercícios
- [x] Treinos
- [x] Faker
- [x] Relatórios
- [x] Exportação JSON
- [x] Autenticação
- [x] Testes automatizados
- [x] Flask
- [x] Dashboard Web
- [x] Alunos Web
- [x] Planos Web
- [x] Assinaturas Web
- [x] Pagamentos Web
- [x] Controle de Acesso Web
- [x] Relatórios Web
- [x] Exportação JSON Web
- [x] Responsividade Web
- [x] Validação `320 x 800`
- [x] Acesso pelo celular
- [x] QR Code
- [x] Testes Web
- [x] 35 testes aprovados
- [x] Versão `0.6.0`

## Próximas etapas

- [ ] Executável com PyInstaller
- [ ] Publicação Web
- [ ] Testes com outros usuários
- [ ] Teste completo após `git clone`
- [ ] Revisão final do GitHub
- [ ] Revisão da documentação
- [ ] Preparação do pitch
- [ ] Versão estável `1.0.0`

---

# Status do projeto

| Componente | Status |
|---|---|
| Arquitetura | Concluído |
| SQLite | Concluído |
| Services | Concluído |
| CLI | Concluída |
| GUI | Concluída |
| Web | Concluída |
| Flask | Concluído |
| JSON | Concluído |
| Faker | Concluído |
| Relatórios | Concluído |
| Autenticação | Concluída |
| Mobile 320 x 800 | Concluído |
| QR Code | Concluído |
| Testes automatizados | 35 aprovados |
| Executável | Não iniciado |
| Deploy | Não iniciado |
| Teste com usuários | Pendente |
| Versão atual | `0.6.0` |
| Versão estável | Não concluída |

---

# Próximas etapas

Com a aplicação Web concluída, os próximos objetivos são:

```text
PyInstaller
    ↓
Executável local
    ↓
Deploy Web
    ↓
Teste com outras pessoas
    ↓
Teste após git clone
    ↓
Revisão final
    ↓
1.0.0
```

---

# Licença

As condições de utilização estão disponíveis em:

```text
LICENSE
```

---

# Autor

Projeto desenvolvido como trabalho final de programação.