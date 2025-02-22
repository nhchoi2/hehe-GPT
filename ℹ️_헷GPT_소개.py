import streamlit as st

# 📌 페이지 설정
st.set_page_config(page_title="ℹ️ 헷GPT 소개", page_icon="ℹ️", layout="wide")

# 📌 CSS 적용 (모던 카드 스타일)
st.markdown("""
    <style>
        body {
            background-color: #f8f9fa;
            font-family: 'Poppins', sans-serif;
        }
        .card {
            background: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
            margin-bottom: 20px;
        }
    </style>
""", unsafe_allow_html=True)

# 📌 ℹ️ 헷GPT 소개 페이지 제목
st.markdown('<div class="card">', unsafe_allow_html=True)
st.title("ℹ️ 헷GPT - AI 기반 개발 도우미")
st.subheader("Python & AI를 활용한 차세대 개발 및 학습 도구")
st.markdown("""
헷GPT는 **AI 챗봇, 코드 실행, AI 이미지 생성, 세무 상담** 기능을 통합한 웹 애플리케이션입니다.  
Hugging Face AI 모델과 Pinecone 벡터 검색을 활용하여 **개발자, 데이터 사이언티스트, 연구자** 등 누구나 쉽게 활용할 수 있도록 설계되었습니다.
""")
st.markdown('</div>', unsafe_allow_html=True)

# 📌 ℹ️ 탭을 활용하여 정보 유지 + 섹션 구분
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["📌 개요", "🎯 프로젝트 목적", "🚀 주요 기능", "🤖 사용된 AI 모델", "🔒 보안 & 배포", "🛠 향후 개발 계획"])

# 📌 개요 섹션
with tab1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.header("📌 개요")
    st.write("""
    헷GPT는 Python 및 HTML 코드를 실행하고, AI 챗봇과 대화할 수 있는 웹 애플리케이션입니다.  
    또한, Hugging Face의 AI 모델을 inference하여 다양한 기능을 제공합니다.  
    개발자, 데이터 사이언티스트, 연구자 등 누구나 쉽게 활용할 수 있도록 설계되었습니다.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# 📌 프로젝트 목적 및 활용 사례
with tab2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.header("🎯 프로젝트 목적 및 활용 사례")
    st.markdown("""
    - **AI 기반 개발 보조 도구:** 개발자가 실시간으로 코드 실행, AI 코드 분석 및 디버깅 가능  
    - **빠른 프로토타이핑 환경:** Streamlit 기반의 직관적인 인터페이스 제공  
    - **AI 이미지 생성:** 텍스트 프롬프트를 기반으로 창의적인 비주얼 컨텐츠 제작 가능  
    - **교육 및 학습 보조:** AI를 활용한 코드 실행 및 분석 기능으로 프로그래밍 학습 지원  
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# 📌 주요 기능
with tab3:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.header("🚀 주요 기능")
    st.markdown("""
    - **Python 코드 실행:** 사용자가 입력한 Python 코드를 동적 실행하고, 안전한 샌드박스 환경에서 결과를 반환  
    - **HTML 코드 미리보기:** HTML 코드를 직접 입력하고, WebView 컴포넌트를 통해 실시간 렌더링 제공  
    - **AI 챗봇:** Hugging Face의 AI 모델을 활용한 고도화된 대화형 NLP 서비스 (`google/gemma-2-9b-it` 적용)  
    - **Qwen 모델 기반 코드 생성:** `Qwen2.5-Coder-32B-Instruct` 모델을 활용하여 AI 기반 코드 생성 및 리팩토링 지원  
    - **AI 이미지 생성:** Diffusion 모델을 활용하여 텍스트 기반 이미지 생성 (`black-forest-labs/FLUX.1-dev` 적용)  
    - **보안 강화:** `.env` 파일을 사용하여 API 키 보호 및 Streamlit Secrets 설정으로 환경 변수 관리  
    - **Streamlit Cloud 기반 배포:** Streamlit의 무료 클라우드 환경을 활용하여 가볍고 빠른 서비스 제공  
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# 📌 사용된 AI 모델
with tab4:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.header("🤖 사용된 AI 모델")
    st.markdown("""
    - **잼마 모델 (`google/gemma-2-9b-it`)** → AI 챗봇 및 자연어 이해 모델  
    - **Qwen 모델 (`Qwen/Qwen2.5-Coder-32B-Instruct`)** → AI 기반 코드 생성 및 리팩토링 기능  
    - **FLUX 모델 (`black-forest-labs/FLUX.1-dev`)** → Stable Diffusion 기반 AI 이미지 생성  
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# 📌 보안 및 배포 방식
with tab5:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.header("🔒 보안 및 배포")
    st.markdown("""
    - **환경 변수 (.env) 사용** → API 키, Hugging Face 토큰 등을 `.env` 파일에 저장하여 보안 유지  
    - **Streamlit Secrets 사용** → 배포 환경에서 안전하게 API 키 관리 및 클라이언트 인증  
    - **Streamlit Cloud 배포** → 추가적인 서버 없이 Streamlit Cloud를 활용한 무료 배포  
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# 📌 향후 개발 계획
with tab6:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.header("🛠 향후 개발 계획")
    st.markdown("""
    - **다양한 프로그래밍 언어 지원:** Python 외에도 JavaScript, SQL, Rust 등 다중 언어 실행 지원 예정  
    - **AI 모델 최적화:** Transformer 기반 모델 최적화 및 Fine-tuning 기법 활용하여 응답 속도 개선  
    - **사용자 코드 저장 기능:** 클라우드 기반 코드 저장 및 재실행 기능 추가  
    - **협업 기능 강화:** 실시간 코드 공유 및 다중 사용자 협업 환경 구축  
    """)
    st.markdown('</div>', unsafe_allow_html=True)
