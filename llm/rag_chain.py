from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from .ollama_client import get_ollama_llm

def build_chain():
    llm = get_ollama_llm()
    prompt = PromptTemplate(
        template="""
        당신은 친절하게 답변해주는 AI입니다.

        질문: {question}
        """,
        input_variables=["question"],
    )
    output_parser = StrOutputParser()
    # LCEL(랭체인 언어)로 체인 구축
    chain = prompt | llm | output_parser
    return chain