# Changelog

Todas as alterações relevantes deste projeto serão documentadas neste arquivo.

O projeto utiliza versionamento semântico no formato:

MAJOR.MINOR.PATCH

---

## [0.4.0] - 2026-09-21

### Adicionado

- Exportação completa do banco SQLite para JSON.
- Diretório dedicado para arquivos exportados.
- Usuário administrativo `root master`.
- Autenticação para acesso à exportação JSON.
- Armazenamento da senha administrativa através de hash.
- Máscara visual de senha no terminal.
- Nova tabela `usuarios`.
- Model `Usuario`.
- Serviço de autenticação de usuários.
- Integração da biblioteca Faker.
- Geração automática de alunos fictícios.
- Geração automática de assinaturas fictícias.
- Geração automática de pagamentos fictícios.
- Geração automática de históricos de acesso fictícios.
- Relatório geral da academia.
- Relatório financeiro.
- Relatório de acessos.
- Ranking de frequência dos alunos.
- Relatório de planos.
- Submenu de relatórios na interface CLI.
- Documentação dos papéis de PO, QA, UX, Tech Lead/Dev e IA.
- Estrutura inicial de testes automatizados com Pytest.
- Banco SQLite temporário para execução isolada dos testes.

### Testes

- Teste automático da criação das tabelas.
- Testes de autenticação administrativa.
- Testes de cadastro e consulta de alunos.
- Testes de validação de CPF e e-mail duplicados.
- Testes de cadastro e consulta de planos.
- Teste de duplicidade de planos.
- Testes de geração de cobranças.
- Testes de registro de pagamentos.
- Testes de inadimplência.
- Testes de autorização de acesso.
- Testes de bloqueio de acesso por inadimplência.
- Teste de bloqueio para aluno sem assinatura.
- Testes de histórico de acesso.
- Testes dos relatórios geral, financeiro, acessos e planos.
- 28 testes automatizados executados com sucesso.

### Alterado

- Interface CLI ampliada com opções de Faker e relatórios.
- Exportação JSON passou a exigir autenticação administrativa.
- Relatório financeiro passou a atualizar automaticamente pagamentos vencidos antes da consulta.
- README ampliado com arquitetura, funcionalidades, instalação, autenticação, Faker, relatórios, interfaces planejadas e documentação.

---

## [0.3.0] - 2026-09-19

### Adicionado

- Serviço de gerenciamento de pagamentos.
- Geração de cobranças vinculadas às assinaturas.
- Registro de pagamentos e formas de pagamento.
- Atualização automática de pagamentos pendentes para atrasados.
- Verificação automática de inadimplência.
- Serviço de controle de acesso.
- Autorização automática de acesso para alunos regulares.
- Bloqueio automático de acesso em caso de inadimplência.
- Registro e histórico de acessos.
- Serviço de gerenciamento de exercícios.
- Cadastro e listagem de exercícios.
- Serviço de gerenciamento de treinos.
- Criação de fichas de treino.
- Associação de exercícios às fichas.
- Controle de séries, repetições, carga, descanso e ordem dos exercícios.
- Visualização completa da ficha de treino pela CLI.

### Validado

- Fluxo de pagamento pendente para pago.
- Detecção de pagamento atrasado.
- Acesso autorizado para aluno regular.
- Acesso negado por inadimplência.
- Persistência do histórico de acessos.
- Criação e consulta de fichas de treino.

---

## [0.2.0] - 2026-09-19

### Adicionado

- Primeira interface CLI funcional.
- Serviço de gerenciamento de alunos.
- Cadastro de alunos no banco SQLite.
- Listagem de alunos cadastrados.
- Busca de alunos por ID.
- Busca de alunos por CPF.
- Serviço de gerenciamento de planos.
- Cadastro e listagem de planos.
- Busca de planos por ID e nome.
- Serviço de gerenciamento de assinaturas.
- Associação entre aluno e plano.
- Listagem de assinaturas.
- Verificação de assinatura ativa por aluno.
- Menu interativo pelo terminal.
- Entrada de dados pelo usuário.

### Corrigido

- Entrada de data de nascimento adaptada para o formato brasileiro DD/MM/AAAA.
- Validação para impedir duplicidade de CPF e e-mail no cadastro de alunos.
- Validação para impedir duplicidade de nomes de planos.
- Verificação para evitar múltiplas assinaturas ativas para o mesmo aluno.

---

## [0.1.0] - 2026-09-19

### Adicionado

- Estrutura inicial do projeto.
- Organização dos módulos CLI, GUI e Web.
- Estrutura para banco de dados.
- Models de Aluno, Plano, Assinatura, Pagamento, Acesso, Treino e Exercício.
- Banco de dados SQLite.
- Criação automática das tabelas.
- Tabela de relacionamento entre treinos e exercícios.
- Diretório para exportação de dados em JSON.
- Diretório para documentação.
- Diretório para testes.
- Arquivo de versionamento.
- Arquivos iniciais de configuração do projeto.