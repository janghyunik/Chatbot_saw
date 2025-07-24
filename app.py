import gradio as gr
from llm.rag_chain import build_chain

chain = build_chain()

def handle_submit(query, history):
    """질문 입력 시 LLM으로부터 답변 받고, 채팅창 갱신"""
    try:
        # history: [(user, bot), ...] 쌍의 리스트
        response = chain.invoke({"question": query})
        history = history or []
        history.append((query, response))
        return "", history  # 텍스트박스는 비우고, 채팅창은 갱신
    except Exception as e:
        history = history or []
        history.append((query, f"에러: {e}"))
        return "", history

def clear_fields():
    """모든 입력/출력 초기화"""
    return "", []

with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("### AI assistant")

    chatbot = gr.Chatbot(label="Chatbot", height=600, show_copy_button=True)
    query = gr.Textbox(label="질문을 입력하세요", placeholder="예시: 오늘 날씨는?", lines=1)

    with gr.Row():
        btn = gr.Button("Generate")
        clear_btn = gr.Button("Clear")

    # 예시 질문 제공
    gr.Examples(
        examples=["삼성전자에 대해서 설명해줘", "DDR5가 뭐야?"],
        inputs=[query]
    )

    # 이벤트 바인딩
    query.submit(handle_submit, [query, chatbot], [query, chatbot])
    btn.click(handle_submit, [query, chatbot], [query, chatbot])
    clear_btn.click(clear_fields, None, [query, chatbot])

if __name__ == "__main__":
    demo.launch()