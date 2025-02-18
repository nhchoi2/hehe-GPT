import streamlit as st  # 웹 UI 생성을 위한 Streamlit 라이브러리 임포트
from huggingface_hub import InferenceClient  # Hugging Face Inference API 사용을 위한 클라이언트 임포트
import os  # 운영체제 관련 기능 사용 (환경 변수 로드 등)
from dotenv import load_dotenv  # .env 파일에서 환경 변수를 불러오기 위한 라이브러리


# 환경 변수 로드
load_dotenv()  # .env 파일에서 환경 변수들을 불러옵니다.
api_key = os.getenv("HUGGINGFACE_API_KEY")  # 환경 변수에서 HUGGINGFACE_API_KEY 값을 가져옵니다.


# 인터넷창 열면 표시되는 이미지 및 이름 (탭이름)
st.set_page_config(
    page_title="코드헷GPT",  # 브라우저 탭에 표시될 페이지 제목 설정
    page_icon="🤖",  # 페이지 아이콘 설정 (이모지 사용 가능)
    layout="wide"  # 페이지 레이아웃을 와이드 모드로 설정하여 넓게 사용
)


# 사이드바 초기화 버튼
if st.sidebar.button("대화 기록 초기화"):
    # 만약 사이드바의 '대화 기록 초기화' 버튼을 누르면
    st.session_state.chat_history = []  # 세션 상태에서 'chat_history' 변수를 빈 리스트로 초기화하여 대화 기록 삭제


# 대화 기록 초기화 및 세션 상태 확인
if "chat_history" not in st.session_state or not isinstance(st.session_state.chat_history, list):
    # 만약 'chat_history'가 세션 상태에 존재하지 않거나, 리스트가 아닐 경우
    st.session_state.chat_history = []  # 'chat_history'를 빈 리스트로 초기화하여 정상적으로 작동하도록 설정

# 페이지 제목 및 설명 표시
st.title("🤖 코드헷GPT")  
st.write("코드를 입력하면 헷GPT가 개선점, 디버깅 방법 등을 안내해드립니다!")  


# Hugging Face InferenceClient 초기화
client = InferenceClient(provider="hf-inference", api_key=api_key)  # API 키를 사용해 Hugging Face Inference Client 생성


# 기존 대화 기록 출력
for chat in st.session_state.chat_history:
    # 세션 상태에서 저장된 대화 기록(chat_history)을 순회하며 하나씩 출력
    if isinstance(chat, dict) and "role" in chat and "content" in chat:  # 데이터 형식이 올바른지 확인
        if chat["role"] == "user":
            st.chat_message("user").write(chat["content"])  # 사용자가 입력한 메시지를 UI에 표시
        else:
            st.chat_message("assistant").write(chat["content"])  # AI가 생성한 응답을 UI에 표시
    else:
        st.warning("올바르지 않은 대화 데이터가 감지되었습니다. 일부 메시지는 표시되지 않을 수 있습니다.")  # 비정상적인 데이터가 감지될 경우 경고 메시지 출력


# 사용자 입력 받기 (대화형 입력창)
user_input = st.chat_input("코드를 입력하세요:")  # 사용자가 코드를 입력할 수 있는 대화형 입력창 제공


# 사용자 입력 처리 및 AI 응답 생성
if user_input:
    # 사용자가 입력한 내용을 chat_history에 추가하고 UI에 표시
    st.session_state.chat_history.append({"role": "user", "content": user_input})  # 사용자 입력을 기록
    st.chat_message("user").write(user_input)  # UI에 사용자 입력 표시

    # AI 응답 생성 요청: 지금까지의 대화 기록을 전달하여 문맥 기반 응답을 생성
    with st.spinner("헷GPT가 응답을 생성 중입니다..."):
        response = client.chat.completions.create(
            model="Qwen/Qwen2.5-Coder-32B-Instruct",  # 코드 관련 질문에 특화된 AI 모델 사용
            messages=st.session_state.chat_history,  # 현재까지의 대화 기록을 API에 전달
            max_tokens=1024,  # 최대 응답 길이를 1024 토큰으로 제한하여 효율적인 응답 생성
        )
        assistant_message = response.choices[0].message.content  # AI 응답에서 메시지 내용 추출

    # 생성된 AI 응답을 대화 기록에 추가하고 UI에 표시
    st.session_state.chat_history.append({"role": "assistant", "content": assistant_message})  # AI 응답을 기록
    st.chat_message("assistant").write(assistant_message)  # AI의 응답을 UI에 표시
