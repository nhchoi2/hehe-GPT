import streamlit as st
from huggingface_hub import InferenceClient
from dotenv import load_dotenv
import os

# 환경 변수 로드
load_dotenv()
api_key = os.getenv("HUGGINGFACE_API_KEY")

# Hugging Face API 설정
client = InferenceClient(provider="hf-inference", api_key=api_key)

# Streamlit UI 설정
st.set_page_config(page_title="AI 고객 상담 챗봇", page_icon="💬", layout="wide")

st.title("💬 맞춤형 AI 고객 상담 챗봇")
st.write("고객님의 질문을 입력하면 AI가 답변해드립니다.")

# 대화 기록 저장
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# AI 응답 처리 함수
def get_response():
    user_input = st.session_state.chat_input
    if user_input:
        with st.spinner("AI가 답변을 생성 중입니다..."):
            response = client.chat.completions.create(
                model="google/gemma-2-9b-it", 
                messages=[{"role": "user", "content": user_input}], 
                max_tokens=1024,
            ).choices[0].message.content
            
            # 대화 기록 저장
            st.session_state.chat_history.insert(0, ("👤 사용자:", user_input))
            st.session_state.chat_history.insert(0, ("🤖 AI:", response))
            st.session_state.pop("chat_input", None)

# 대화 출력 (최신 메시지가 위로)
st.markdown("### 대화 기록")
for role, message in reversed(st.session_state.chat_history):
    st.markdown(f"**{role}** {message}")

# 입력 필드
st.chat_input("질문을 입력하세요:", key="chat_input", on_submit=get_response)

st.write("이 챗봇은 고객 상담 및 AI 지원을 제공합니다. 🚀")
