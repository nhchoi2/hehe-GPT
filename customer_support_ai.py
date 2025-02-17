import streamlit as st
from huggingface_hub import InferenceClient
from dotenv import load_dotenv
import os

# 환경 변수 로드
load_dotenv()
api_key = os.getenv("HUGGINGFACE_API_KEY")

# Hugging Face API 설정
client = InferenceClient(
    provider="hf-inference",
    api_key=api_key
)

# Streamlit UI 설정
st.set_page_config(page_title="AI 고객 상담 챗봇", page_icon="💬", layout="wide")

st.markdown(
    """
    <style>
        .stTextInput > div > div > input {
            font-size: 16px;
            padding: 10px;
            border-radius: 10px;
        }
        .stButton > button {
            background-color: #007BFF;
            color: white;
            font-size: 16px;
            border-radius: 10px;
            padding: 10px 20px;
        }
        .stMarkdown {
            font-size: 18px;
            line-height: 1.6;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("💬 맞춤형 나만의 AI 헤헤^^ GPT")
st.write("고객님의 질문을 입력하면 AI가 답변해드립니다.")

# 대화 기록을 저장할 공간 초기화
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# 대화 출력 (최신 메시지가 위로 오도록 역순 정렬)
st.markdown("### 대화 기록")
chat_container = st.container()
with chat_container:
    for role, message in reversed(st.session_state.chat_history):  # 최신 메시지가 위로 오도록 변경
        st.markdown(f"**{role}** {message}")

# 사용자 입력 받기
col1, col2 = st.columns([4, 1])

def get_response():
    user_input = st.session_state.user_input
    if user_input:
        with st.spinner("AI가 답변을 생성 중입니다..."):
            messages = [{"role": "user", "content": user_input}]
            completion = client.chat.completions.create(
                model="google/gemma-2-9b-it", 
                messages=messages, 
                max_tokens=1024,
            )
            response = completion.choices[0].message.content
            
            # 대화 기록 저장
            st.session_state.chat_history.insert(0, ("👤 사용자:", user_input))
            st.session_state.chat_history.insert(0, ("🤖 헤헤^^ GPT:", response))
            
            
            # 입력 필드 초기화
            st.session_state.user_input = ""

# 입력 필드 & 버튼 배치
with col1:
    st.text_input("질문을 입력하세요:", key="user_input", on_change=get_response, placeholder="여기에 질문을 입력하세요...")


st.markdown("---")
st.write("이 챗봇은 고객 상담 및 AI 지원을 제공합니다. 🚀")
