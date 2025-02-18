import streamlit as st  # Streamlit 라이브러리 불러오기
from huggingface_hub import InferenceClient  # Hugging Face API 클라이언트 불러오기
from dotenv import load_dotenv  # 환경 변수 로드를 위한 라이브러리
import os  # 운영 체제 관련 기능을 위한 라이브러리

# 환경 변수 로드
load_dotenv()  # .env 파일에서 환경 변수 불러오기
api_key = os.getenv("HUGGINGFACE_API_KEY")  # API 키 가져오기

# Hugging Face API 설정
client = InferenceClient(provider="hf-inference", api_key=api_key)  # Hugging Face API 클라이언트 초기화

# Streamlit UI 설정
st.set_page_config(page_title="헷GPT", page_icon="💬", layout="wide")  # 페이지 제목, 아이콘 및 레이아웃 설정

# 사이드바 추가
with st.sidebar:
    st.header("📌 설정")  # 사이드바 헤더
    clear_chat = st.button("💬 대화 기록 초기화")  # 대화 기록 초기화 버튼
    
    if clear_chat:
        st.session_state.chat_history = []  # 대화 기록 초기화
        st.success("대화 기록이 초기화되었습니다.")  # 성공 메시지 출력

# 메인 제목 및 설명
st.title("💬 똑똑한 AI 헷GPT")  # 메인 페이지 제목
st.write("질문을 입력하면 헷GPT가 답변해드립니다.")  # 페이지 설명

# 대화 기록 저장
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []  # 세션 상태에 대화 기록이 없으면 초기화

# AI 응답 처리 함수
def get_response():
    user_input = st.session_state.chat_input  # 사용자가 입력한 텍스트 가져오기
    if user_input:
        with st.spinner("헷GPT가 답변을 생성 중입니다..."):  # AI 응답 생성 중 스피너 표시
            response = client.chat.completions.create(
                model="google/gemma-2-9b-it",  # 사용 모델 지정
                messages=[{"role": "user", "content": user_input}],  # 사용자 메시지 전달
                max_tokens=1024,  # 최대 토큰 설정
            ).choices[0].message.content  # 응답 메시지 추출
            
            # 대화 기록 저장
            st.session_state.chat_history.insert(0, ("👤 사용자:", user_input))  # 사용자 입력 저장
            st.session_state.chat_history.insert(0, ("🤖 헷GPT:", response))  # AI 응답 저장
            st.session_state.pop("chat_input", None)  # 입력 필드 초기화

# 대화 출력 (최신 메시지가 위로)
st.markdown("### 대화 기록")  # 대화 기록 섹션 제목 출력
for role, message in reversed(st.session_state.chat_history):  # 대화 기록을 역순으로 출력
    st.markdown(f"**{role}** {message}")

# 입력 필드
st.chat_input("질문을 입력하세요:", key="chat_input", on_submit=get_response)  # 사용자 입력 필드 설정 및 응답 함수 연결
