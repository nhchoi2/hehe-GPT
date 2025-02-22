import streamlit as st

# 페이지 설정
st.set_page_config(page_title="헷GPT 소개", layout="wide")
st.markdown("""
<style>
    .stTextInput, .stTextArea {
        border-radius: 10px;
        padding: 10px;
        background-color: #ffffff;
        box-shadow: 0px 2px 10px rgba(0, 0, 0, 0.1);
    }
</style>
""", unsafe_allow_html=True)

# 제목
st.title("헷GPT: 실시간 코드 실행 및 AI 챗봇")

# 개요
st.header("개요")
st.write(
    "헷GPT는 Python 및 HTML 코드를 실행하고, AI 챗봇과 대화할 수 있는 웹 애플리케이션입니다. "
    "또한, Hugging Face의 AI 모델을 inference하여 다양한 기능을 제공합니다. "
    "개발자, 데이터 사이언티스트, 연구자 등 누구나 쉽게 활용할 수 있도록 설계되었습니다."
)

# 프로젝트 목적과 활용 사례
st.header("프로젝트 목적 및 활용 사례")
st.markdown("""
- **AI 기반 개발 보조 도구:** 개발자가 실시간으로 코드 실행, AI 코드 분석 및 디버깅 가능
- **빠른 프로토타이핑 환경:** Streamlit 기반의 직관적인 인터페이스 제공
- **AI 이미지 생성:** 텍스트 프롬프트를 기반으로 창의적인 비주얼 컨텐츠 제작 가능
- **교육 및 학습 보조:** AI를 활용한 코드 실행 및 분석 기능으로 프로그래밍 학습 지원
""")

# 주요 기능
st.header("주요 기능")
st.markdown("""
- **Python 코드 실행:** 사용자가 입력한 Python 코드를 동적 실행하고, 안전한 샌드박스 환경에서 결과를 반환
- **HTML 코드 미리보기:** HTML 코드를 직접 입력하고, WebView 컴포넌트를 통해 실시간 렌더링 제공
- **AI 챗봇:** Hugging Face의 AI 모델을 활용한 고도화된 대화형 NLP 서비스 (`google/gemma-2-9b-it` 적용)
- **Qwen 모델 기반 코드 생성:** `Qwen2.5-Coder-32B-Instruct` 모델을 활용하여 AI 기반 코드 생성 및 리팩토링 지원
- **AI 이미지 생성:** Diffusion 모델을 활용하여 텍스트 기반 이미지 생성 (`black-forest-labs/FLUX.1-dev` 적용)
- **보안 강화:** `.env` 파일을 사용하여 API 키 보호 및 Streamlit Secrets 설정으로 환경 변수 관리
- **Streamlit Cloud 기반 배포:** Streamlit의 무료 클라우드 환경을 활용하여 가볍고 빠른 서비스 제공
""")

# 사용된 인공지능 모델
st.header("사용된 AI 모델")
st.markdown("""
- **잼마 모델 (`google/gemma-2-9b-it`)** → AI 챗봇 및 자연어 이해 모델
- **Qwen 모델 (`Qwen/Qwen2.5-Coder-32B-Instruct`)** → AI 기반 코드 생성 및 리팩토링 기능
- **FLUX 모델 (`black-forest-labs/FLUX.1-dev`)** → Stable Diffusion 기반 AI 이미지 생성
""")

# 보안 및 배포 방식
st.header("보안 및 배포")
st.markdown("""
- **환경 변수 (.env) 사용** → API 키, Hugging Face 토큰 등을 `.env` 파일에 저장하여 보안 유지
- **Streamlit Secrets 사용** → 배포 환경에서 안전하게 API 키 관리 및 클라이언트 인증
- **Streamlit Cloud 배포** → 추가적인 서버 없이 Streamlit Cloud를 활용한 무료 배포
""")

# 각 페이지로 이동하기
st.header("각 기능 페이지 바로 가기")
st.markdown("""
각 기능별 페이지를 클릭하여 직접 사용해보세요(화면 왼쪽 메뉴바 이용)

- [🤗 헷GPT (챗봇 페이지)]
- [🤖 코드 헷GPT (AI 코드 분석 페이지)]
- [🎨 화가 헷GPT (AI 이미지 생성 페이지)]
- [💻 실행 헷GPT (코드 실행 페이지)]
""")

# 향후 개발 계획
st.header("향후 개발 계획")
st.markdown("""
- **다양한 프로그래밍 언어 지원:** Python 외에도 JavaScript, SQL, Rust 등 다중 언어 실행 지원 예정
- **AI 모델 최적화:** Transformer 기반 모델 최적화 및 Fine-tuning 기법 활용하여 응답 속도 개선
- **사용자 코드 저장 기능:** 클라우드 기반 코드 저장 및 재실행 기능 추가
- **협업 기능 강화:** 실시간 코드 공유 및 다중 사용자 협업 환경 구축
- **RAG(Retrieval-Augmented Generation) 기술을 도입하여, AI 질의응답 시스템을 구축
""")

# 배포 환경 정보
st.header("배포 환경")
st.markdown("""
헷GPT는 **Streamlit Cloud**에서 호스팅되며, 사용자는 별도의 설정 없이 웹 브라우저에서 바로 사용할 수 있습니다. 
배포는 **Streamlit Secrets**을 활용하여 API 키를 보호하고 있으며, 간편한 배포 환경을 제공합니다.
""")
