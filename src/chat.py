import os
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_postgres import PGVector
from langchain_openai import OpenAIEmbeddings

load_dotenv()

for k in("OPENAI_API_KEY", "PGVECTOR_URL", "PGVECTOR_COLLECTION"):
    if not os.getenv(k):
        raise RuntimeError(f"Environment variable: {k} is not set")

embeddings = OpenAIEmbeddings(model=os.getenv("OPENAI_EMBEDDING_MODEL", "text-embedding-3-small"))

store = PGVector(
    embeddings=embeddings,
    collection_name=os.getenv("PGVECTOR_COLLECTION"),
    connection=os.getenv("PGVECTOR_URL"),
    use_jsonb=True,
)

resultados = store.similarity_search(
    "Qual o faturamento da Empresa SuperTechIABrazil?",
    k=10
)

llm = ChatOpenAI(
    model=os.getenv("OPENAI_CHAT_MODEL", "gpt-4.1"),
    temperature=0,
)

def montar_prompt(contexto, pergunta):
    return f"""
CONTEXTO:
{contexto}

REGRAS OBRIGATÓRIAS:
1. Use exclusivamente informações textualmente presentes no CONTEXTO.
2. Não faça cálculos, contagens, resumos ou interpretações.
3. Não deduza informações implícitas.
4. Não use conhecimento externo.
5. Se encontrar valor em R$, responda no formato: O faturamento da Empresa X é R$ valor de reais.
6. Se a resposta não estiver explicitamente escrita no CONTEXTO, responda exatamente:

Não tenho informações necessárias para responder sua pergunta.

PERGUNTA DO USUÁRIO:
{pergunta}

RESPONDA A PERGUNTA DO USUÁRIO:
"""

def chat():
    print("Chat iniciado (digite 'sair' para encerrar)\n")

    while True:
        pergunta = input("Você: ")

        if pergunta.lower() in ["sair", "exit", "quit"]:
            break
        
        resultados = store.similarity_search(pergunta, k=10)

        contexto = "\n\n".join([doc.page_content for doc in resultados])

        prompt = montar_prompt(contexto, pergunta)

        resposta = llm.invoke(prompt)

        print("\n\n Resposta:\n", resposta.content)
        print("\n" + "-"*50 + "\n")

if __name__ == "__main__":
    chat()
