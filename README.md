# Desafio MBA FullCycle Ingestão e Busca
Projeto sobre a Ingestão e Busca Semântica com LangChain e Postgres

# Sobre o projeto
  Desenvolver um software capaz de:
  Ingestão: Ler um arquivo PDF e salvar suas informações em um banco de dados PostgreSQL com extensão pgVector.
  Busca: Permitir que o usuário faça perguntas via linha de comando (CLI) e receba respostas baseadas apenas no conteúdo do PDF.

# Tecnologias utilizadas
  Linguagem de programação: Python 3.12.3
  Framework: LangChain 1.2.15
  Banco de dados: PostgreSQL + pgVector (image: pgvector/pgvector:pg17)
  Docker: 29.3.0

# Como executar o projeto

```bash
  # Clonar o repositório
  git clone https://github.com/luisinho/mba-ia-desafio-ingestao-busca.git
  # Entrar na pasta do projeto
  cd mba-ia-desafio-ingestao-busca
  Crie e ative um ambiente virtual antes de instalar dependências: source venv/bin/activate e source .venv/bin/activate
  Execute o comando: pip install -U langchain==1.2.15 langchain-core langchain-openai langchain-postgres langchain-community langchain-text-splitters
  Subir o banco de dados: docker compose up -d
  Executar o python src/ingest.py para Ingestão no PostgreSQL / pgVector
  Executar o python src/chat.py -> "abri o terminal para e pergunta e se digitar sair é desconectado do terminal CLI"
  Executar o search.py Script de busca similarity_search

# Autor

Luis Antonio Batista dos Santos

https://www.linkedin.com/in/luis-antonio-batista-dos-santos-5a37b781
