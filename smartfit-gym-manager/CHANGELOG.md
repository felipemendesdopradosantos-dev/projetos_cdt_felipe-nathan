# Changelog

Todas as alterações relevantes deste projeto serão documentadas neste arquivo.

O projeto utiliza versionamento semântico no formato:

MAJOR.MINOR.PATCH

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