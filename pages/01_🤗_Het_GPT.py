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

# 현재 페이지에 대한 고유한 키 생성 (페이지별 대화 기록 유지)
current_page = "ai_het_assistant"  # 현재 페이지의 고유한 식별자
page_key = f"chat_history_{current_page}"

# 페이지별 대화 기록 초기화
if page_key not in st.session_state:
    st.session_state[page_key] = []
# 사이드바 추가
with st.sidebar:
    st.header("📌 설정")  # 사이드바 헤더
    clear_chat = st.button("💬 대화 기록 초기화")  # 대화 기록 초기화 버튼
    
    if clear_chat:
        st.session_state[page_key] = []  # 대화 기록 초기화
        st.success("대화 기록이 초기화되었습니다.")  # 성공 메시지 출력

# 메인 제목 및 설명
st.title("💬 똑똑한 AI 헷GPT")  # 메인 페이지 제목
st.write("질문을 입력하면 헷GPT가 답변해드립니다.")  # 페이지 설명

# 대화 기록 저장
if "chat_history" not in st.session_state:
    st.session_state[page_key] = []  # 세션 상태에 대화 기록이 없으면 초기화

# AI 응답 처리 함수
def get_response():
    # 올바른 입력 값 가져오기 (입력 필드는 "chat_input"에 저장됩니다)
    user_input = st.session_state.chat_input  
    if user_input:
        # 기존 대화 기록을 메시지 리스트로 변환 (오래된 순서대로)
        conversation_messages = []
        # 저장된 대화 기록은 최신 메시지가 앞에 있으므로, 역순으로 정렬합니다.
        for role, message in reversed(st.session_state[page_key]):
            if role.startswith("👤"):  # 사용자 메시지인 경우
                conversation_messages.append({"role": "user", "content": message})
            elif role.startswith("🤖"):  # 헷GPT(assistant) 메시지인 경우
                conversation_messages.append({"role": "assistant", "content": message})
        # 현재 사용자의 입력도 추가합니다.
        conversation_messages.append({"role": "user", "content": user_input})
        
        with st.spinner("헷GPT가 답변을 생성 중입니다..."):
            response = client.chat.completions.create(
                model="google/gemma-2-9b-it",
                messages=conversation_messages,  # 대화 이력을 포함한 메시지 리스트 전달
                max_tokens=1024,
            ).choices[0].message.content
            
            # 대화 기록 업데이트 (최신 메시지가 위에 표시되도록)
            st.session_state[page_key].insert(0, ("🤖 헷GPT:", response))
            st.session_state[page_key].insert(0, ("👤 사용자:", user_input))
            st.session_state.pop("chat_input", None)
            
# 대화 출력 (최신 메시지가 위로)
st.markdown("### 대화 기록")  # 대화 기록 섹션 제목 출력
for role, message in reversed(st.session_state[page_key]):  # 대화 기록을 역순으로 출력
    st.markdown(f"**{role}** {message}")

# 입력 필드
st.chat_input("질문을 입력하세요:", key="chat_input", on_submit=get_response)  # 사용자 입력 필드 설정 및 응답 함수 연결
