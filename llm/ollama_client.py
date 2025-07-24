# ollama_client.py
from langchain_ollama import ChatOllama
from dotenv import load_dotenv
import os

# 환경변수 및 모델 로드
load_dotenv()
MODEL = os.getenv("LLM_MODEL")

def get_ollama_llm(model_name=MODEL):
    return ChatOllama(model=model_name)