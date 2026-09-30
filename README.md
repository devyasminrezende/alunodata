# AlunoData

O **AlunoData** é uma aplicação desenvolvida em Python para gerenciamento e análise de dados de alunos. O sistema permite cadastrar, listar, buscar, atualizar, excluir e ordenar registros, além de realizar tratamento e análise dos dados. A aplicação valida os registros, remove dados inválidos da análise, padroniza informações textuais, identifica matrículas duplicadas, calcula a idade média e apresenta a quantidade de alunos por curso e por cidade por meio de um relatório. Os dados são persistidos em um arquivo JSON, utilizando `json` e `pathlib`, sem necessidade de bibliotecas externas.

## Funcionalidades

- Cadastro, consulta, atualização e exclusão de alunos;
- Busca por nome ou matrícula;
- Ordenação por nome, idade ou curso;
- Validação e limpeza dos dados;
- Padronização de informações;
- Identificação de matrículas duplicadas;
- Cálculo da idade média;
- Análise por curso e cidade;
- Geração de relatório dos dados.

## Estrutura

```text
alunodata/
├── data/
│   └── alunos.json
├── src/
│   ├── main.py
│   └── analise.py
├── .gitignore
└── README.md
Como executar

É necessário ter o Python 3 instalado. No terminal, execute:
python src/main.py
No Windows, caso necessário:
py src/main.py
Os dados utilizados pela aplicação são armazenados em data/alunos.json.

Possíveis melhorias

Como evolução do projeto, podem ser adicionados testes automatizados, banco de dados, API, logs e validações mais completas.