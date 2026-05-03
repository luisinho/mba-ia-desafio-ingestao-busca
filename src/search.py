import os
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_postgres import PGVector

load_dotenv()

for k in("OPENAI_API_KEY", "PGVECTOR_URL", "PGVECTOR_COLLECTION"):
    if not os.getenv(k):
        raise RuntimeError(f"Environment variable: {k} is not set")

queries = [
    "Qual o faturamento da Empresa SuperTechIABrazil",
    "Aurora Eventos ME",
    "Empresa turismo azul"
]

embeddings = OpenAIEmbeddings(model=os.getenv("OPENAI_EMBEDDING_MODEL", "text-embedding-3-small"))

store = PGVector(
    embeddings=embeddings,
    collection_name=os.getenv("PGVECTOR_COLLECTION"),
    connection=os.getenv("PGVECTOR_URL"),
    use_jsonb=True,
)

for q in queries:
    print(f"\nConsulta: {q}")
    results = store.similarity_search_with_score(query=q, k=3)

    print("\nTop 1 resultados encontrados:\n")

    for i, (doc, score) in enumerate(results, start=1):
        print("=" * 60)
        print(f"Resultado {i}")
        print(f"Score Similaridade: {score}")
        print("Conteúdo:")
        print(doc.page_content.strip())
        print("=" * 60)