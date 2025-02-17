import streamlit as st

# 앱 소개 페이지
st.set_page_config(page_title="앱 소개", page_icon="ℹ️", layout="wide")

st.title("ℹ️ 헷GPT 소개")

st.markdown(
    """
    ## 🤖 헷GPT란?
    헷GPT는 고객 지원 및 AI 기반 상담을 제공하는 맞춤형 챗봇입니다.
    사용자의 질문을 분석하고 AI가 적절한 답변을 제공합니다.
    
    ---
    
    ## 주요 기능
    - **AI 기반 고객 상담**: 다양한 고객 문의를 이해하고 해결책을 제안
    - **실시간 응답**: 질문 입력 후 빠르게 AI 답변 생성
    - **대화 기록 유지**: 사용자의 대화 내용을 저장하여 지속적인 대화 가능
    - **모델 초기화 기능**: 필요할 때 AI 모델을 재설정
    
    ---
    
    ## 🛠️ 사용 기술 & 보안
    - Hugging Face API (google/gemma-2-9b-it 모델 사용) → AI 기반 자연어 처리
    - Streamlit을 활용한 웹 기반 UI → 직관적인 사용자 인터페이스 제공
    - Python 및 NLP 기반 자연어 처리 → 대화형 챗봇 기능 구현

    ---

    ## 🔒 보안 및 데이터 보호
    - 환경 변수 (.env) 사용 → API 키 및 민감한 정보 보호
    - .gitignore 설정 → .env 파일을 GitHub에 업로드하지 않도록 방지
    - Streamlit Cloud Secrets Manager 활용 → 안전한 API 키 관리
    - HTTPS 통신 사용 → 네트워크 상에서 데이터 암호화
    - 대화 기록 관리 → session_state를 활용해 사용자 데이터 보호
    
    ---
    
    ##  어떻게 사용하나요?
    1. **사이드바에서 설정을 조정**할 수 있습니다.
    2. **질문을 입력하면 AI가 자동으로 응답**을 생성합니다.
    3. **대화 기록을 유지하며, 필요 시 초기화**할 수 있습니다.
    
    ---
    
    📌 [홈으로 돌아가기](./)
    """,
    unsafe_allow_html=True
)