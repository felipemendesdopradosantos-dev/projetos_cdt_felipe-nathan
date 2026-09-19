# SmartFit Gym Manager

Sistema automatizado de gerenciamento de academia desenvolvido como projeto final do curso de programação.

## Versão

0.1.0

## Objetivo

Desenvolver uma aplicação em Python capaz de automatizar processos relacionados ao gerenciamento de uma academia, utilizando como referência processos e características da Smart Fit.

O sistema deverá permitir o gerenciamento de:

- alunos;
- planos;
- pagamentos;
- controle de acesso e frequência;
- fichas de treino;
- relatórios.

## Tecnologias previstas

- Python
- SQLite
- JSON
- Faker
- Tkinter
- Flask
- HTML
- CSS
- QR Code
- PyInstaller

## Interfaces previstas

O sistema será desenvolvido progressivamente em três interfaces:

1. CLI — interface pelo terminal;
2. GUI — interface gráfica com Tkinter;
3. Web — aplicação executada através de servidor web.

## Banco de dados

O banco principal será desenvolvido utilizando SQLite.

Também será implementada uma funcionalidade para exportação dos dados em formato JSON.

## Estrutura do projeto

```text
smartfit-gym-manager/
├── app/
│   ├── cli/
│   ├── database/
│   ├── gui/
│   ├── models/
│   ├── services/
│   └── web/
├── data/
│   └── exports/
├── docs/
├── tests/
├── .gitignore
├── CHANGELOG.md
├── LICENSE
├── main.py
├── README.md
├── requirements.txt
└── VERSION