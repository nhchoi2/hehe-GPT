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

# 페이지별 대화 기록 초기화 (중복 없이 한 번만 초기화)
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

# AI 응답 처리 함수
def get_response():
    # 올바른 입력 값 가져오기 (입력 필드는 "chat_input"에 저장됩니다)
    user_input = st.session_state.chat_input  
    if user_input:
        # 기존 대화 기록을 메시지 리스트로 변환 (오래된 순서대로)
        # 기존 대화 기록을 하나의 문자열로 합치기
            conversation_history = ""
            for role, message in st.session_state[page_key]:
                conversation_history += f"{role} {message}\n"
            
            # 프롬프트 생성 시 대화 기록을 포함
            system_prompt = """
                당신은 친절하고, 전문적인 한국인 비서입니다. 항상 친절하고 자세하게 답변하세요.
                사용자가 질문을 입력하면, 해당 질문에 대해 전문적인 답변을 제공합니다.
                ...
            """
            # 전체 프롬프트 구성
            prompt = f"{system_prompt}\n대화 기록:\n{conversation_history}\nContext:\n{context}\n\n사용자: {user_input}\n모델:"
                
            with st.spinner("헷GPT가 답변을 생성 중입니다..."):
                response = client.chat.completions.create(
                    model="google/gemma-2-9b-it",
                    messages=[{"role": "user", "content": prompt}],  # 대화 이력을 포함한 메시지 리스트 전달
                    max_tokens=1024,
                ).choices[0].message.content
                
                # 대화 기록 업데이트 (최신 메시지가 위에 표시되도록)
                st.session_state[page_key].insert(0, ("👤 사용자:", user_input))
                st.session_state[page_key].insert(0, ("🤖 헷GPT:", response))
                st.session_state.pop("chat_input", None)
            
# 대화 출력 (최신 메시지가 위로)
st.markdown("### 대화 기록")  # 대화 기록 섹션 제목 출력
for role, message in reversed(st.session_state[page_key]):  # 대화 기록을 역순으로 출력
    st.markdown(f"**{role}** {message}")

# 입력 필드
st.chat_input("질문을 입력하세요:", key="chat_input", on_submit=get_response)  # 사용자 입력 필드 설정 및 응답 함수 연결
