import streamlit as st
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage

# .env 読み込み（ローカル用）
load_dotenv()

st.title("専門家LLM相談アプリ")
st.write("""
このアプリでは、入力した質問に対して  
**選択した専門家の立場**でLLMが回答します。
""")

# 専門家選択
expert = st.radio(
    "専門家を選んでください",
    ("A：ITエンジニア", "B：ビジネスコンサルタント")
)

user_input = st.text_input("質問を入力してください")

def get_llm_response(text: str, expert_type: str) -> str:
    if expert_type.startswith("A"):
        system_prompt = "あなたは経験豊富なITエンジニアです。技術的に正確に答えてください。"
    else:
        system_prompt = "あなたは優秀なビジネスコンサルタントです。分かりやすく助言してください。"

    llm = ChatOpenAI(
        model_name="gpt-4o-mini",
        temperature=0
    )

    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=text)
    ]

    response = llm(messages)
    return response.content

if st.button("送信") and user_input:
    answer = get_llm_response(user_input, expert)
    st.subheader("回答")
    st.write(answer)