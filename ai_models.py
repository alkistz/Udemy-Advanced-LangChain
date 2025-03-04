from langchain_openai import AzureChatOpenAI, AzureOpenAIEmbeddings

from .settings import settings

llm = AzureChatOpenAI(
    azure_endpoint=settings.AZURE_OPENAI_ENDPOINT,
    api_key=settings.AZURE_OPENAI_API_KEY,
    azure_deployment="gpt-4o",
    openai_api_version="2024-08-01-preview",
)
azure_embeddings_model = AzureOpenAIEmbeddings(
    azure_endpoint=settings.AZURE_OPENAI_EMBEDDING_ENDPOINT,
    api_key=settings.AZURE_OPENAI_EMBEDDING_API_KEY,
    model="text-embedding-3-small",
    openai_api_version="2023-05-15",
    max_retries=3,
    retry_min_seconds=4,  # Min time between retries
    retry_max_seconds=20,  # Max time between retries
    show_progress_bar=True,  # Shows progress of embedding
)
