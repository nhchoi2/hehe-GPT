import streamlit as st  # 웹 UI 생성을 위한 Streamlit 라이브러리 임포트
from huggingface_hub import InferenceClient  # Hugging Face Inference API 사용을 위한 클라이언트 임포트
import os  # 운영체제 관련 기능 사용 (환경 변수 로드 등)
from dotenv import load_dotenv  # .env 파일에서 환경 변수를 불러오기 위한 라이브러리

# ------------------------------------------------------------------------
# 환경 변수 로드
# ------------------------------------------------------------------------
load_dotenv()  # .env 파일에서 환경 변수들을 불러옵니다.
api_key = os.getenv("HUGGINGFACE_API_KEY")  # HUGGINGFACE_API_KEY 환경 변수 값을 가져옵니다.

# ------------------------------------------------------------------------
# Streamlit 페이지 설정
# ------------------------------------------------------------------------
st.set_page_config(
    page_title="코드헷GPT",  # 브라우저 탭에 표시될 페이지 제목
    page_icon="🤖",              # 페이지 아이콘 (이모지 사용)
    layout="wide"               # 페이지 레이아웃을 와이드 모드로 설정
)

# ------------------------------------------------------------------------
# 사이드바: 대화 기록 초기화 버튼
# ------------------------------------------------------------------------
# 사용자가 사이드바에 있는 "대화 기록 초기화" 버튼을 누르면, 대화 기록을 초기화합니다.
if st.sidebar.button("대화 기록 초기화"):
    st.session_state.chat_history = []

# ------------------------------------------------------------------------
# 대화 기록을 저장할 세션 상태 초기화
# ------------------------------------------------------------------------
# st.session_state를 사용해 대화 기록을 저장합니다.
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ------------------------------------------------------------------------
# 페이지 제목 및 설명 표시
# ------------------------------------------------------------------------
st.title("🤖 코드헷GPT")
st.write("코드를 입력하면 헷GPT가 개선점, 디버깅 방법 등을 안내해드립니다!")

# ------------------------------------------------------------------------
# Hugging Face InferenceClient 초기화
# ------------------------------------------------------------------------
# API 키를 사용해 Inference API 클라이언트를 생성합니다.
client = InferenceClient(provider="hf-inference", api_key=api_key)

# ------------------------------------------------------------------------
# 기존 대화 기록 출력
# ------------------------------------------------------------------------
# 이미 저장된 대화 기록(세션 상태)을 화면에 표시합니다.
for chat in st.session_state.chat_history:
    if chat["role"] == "user":
        st.chat_message("user").write(chat["content"])  # 사용자 메시지 출력
    else:
        st.chat_message("assistant").write(chat["content"])  # AI(어시스턴트) 메시지 출력

# ------------------------------------------------------------------------
# 사용자로부터 코드 입력 받기 (대화형 입력창)
# ------------------------------------------------------------------------
# st.chat_input()을 사용하여 사용자의 코드를 입력 받습니다.
user_input = st.chat_input("코드를 입력하세요:")

# ------------------------------------------------------------------------
# 사용자 입력 처리 및 AI 응답 생성
# ------------------------------------------------------------------------
if user_input:
    # 사용자 입력 메시지를 대화 기록에 추가하고 화면에 표시합니다.
    st.session_state.chat_history.append({"role": "user", "content": user_input})
    st.chat_message("user").write(user_input)

    # AI 응답 생성 요청: 전체 대화 기록을 모델에 전달하여 문맥 기반 응답을 생성합니다.
    with st.spinner("헷GPT가 응답을 생성 중입니다..."):
        response = client.chat.completions.create(
            model="Qwen/Qwen2.5-Coder-32B-Instruct",  # 코드 관련 질문에 특화된 모델 사용
            messages=st.session_state.chat_history,   # 지금까지의 대화 기록 전달
            max_tokens=1024,                           # 생성될 응답의 최대 토큰 수 설정
        )
        # 모델 응답에서 첫 번째 선택지를 가져옵니다.
        assistant_message = response.choices[0].message.content

    # 생성된 AI 응답을 대화 기록에 추가하고 화면에 표시합니다.
    st.session_state.chat_history.append({"role": "assistant", "content": assistant_message})
    st.chat_message("assistant").write(assistant_message)
