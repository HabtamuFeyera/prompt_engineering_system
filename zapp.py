import os
from langchain.chat_models import ChatOpenAI
from langchain_community.chat_models import ChatOpenAI

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY") or "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"

chat = ChatOpenAI(
    openai_api_key="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",
    model='gpt-3.5-turbo'
)