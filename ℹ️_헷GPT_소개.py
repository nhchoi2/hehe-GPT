import streamlit as st

# 페이지 설정
st.set_page_config(page_title="헷GPT 소개", layout="wide")

# 제목
st.title("헷GPT: 실시간 코드 실행 및 AI 챗봇")

# 개요
st.header("개요")
st.write(
    "헷GPT는 Python 및 HTML 코드를 실행하고, AI 챗봇과 대화할 수 있는 웹 애플리케이션입니다. "
    "또한, Hugging Face의 AI 모델을 inference하여 다양한 기능을 제공합니다. "
    "개발자, 데이터 사이언티스트, 연구자 등 누구나 쉽게 활용할 수 있도록 설계되었습니다."
)

# 주요 기능
st.header("주요 기능")
st.markdown("""
- **Python 코드 실행:** 사용자가 입력한 Python 코드를 동적 실행하고, 안전한 샌드박스 환경에서 결과를 반환
- **HTML 코드 미리보기:** HTML 코드를 직접 입력하고, WebView 컴포넌트를 통해 실시간 렌더링 제공
- **AI 챗봇:** Hugging Face의 AI 모델을 활용한 고도화된 대화형 NLP 서비스 (`google/gemma-2-9b-it` 적용)
- **Qwen 모델 기반 코드 생성:** `Qwen2.5-Coder-32B-Instruct` 모델을 활용하여 AI 기반 코드 생성 및 리팩토링 지원
- **AI 이미지 생성:** Diffusion 모델을 활용하여 텍스트 기반 이미지 생성 (`black-forest-labs/FLUX.1-dev` 적용)
- **보안 강화:** `.env` 파일을 사용하여 API 키 보호 및 Streamlit Secrets 설정으로 환경 변수 관리
- **CI/CD 자동 배포:** GitHub Actions를 활용하여 Streamlit Cloud에 지속적 배포 파이프라인 구축
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
- **GitHub Secrets 사용** → GitHub Actions에서 배포 시 환경 변수 보호 및 CI/CD 적용
- **Streamlit Secrets 사용** → 배포 환경에서 안전하게 API 키 관리 및 클라이언트 인증
- **자동 배포 시스템** → GitHub Actions를 이용한 지속적 통합 및 배포 자동화 (CI/CD 적용)
""")

# 각 페이지별 기능 & 기술 설명
st.header("각 페이지별 기능 & 기술")
st.markdown("""
| 페이지명 | 설명 | 사용 기술 |
|---------|------|----------|
| **ℹ️ 헷GPT 소개** | 프로젝트 개요 및 기능 설명 | Streamlit UI |
| **🤗 헷GPT (챗봇)** | AI 기반 자연어 처리 챗봇 | Hugging Face, `google/gemma-2-9b-it` |
| **🤖 코드 헷GPT** | AI 기반 코드 분석 & 리팩토링 | `Qwen2.5-Coder-32B-Instruct` |
| **🎨 화가 헷GPT** | Diffusion 모델 기반 이미지 생성 | `black-forest-labs/FLUX.1-dev` |
| **💻 실행 헷GPT** | Python & HTML 코드 실행 및 미리보기 | `exec()`, `streamlit.components.v1.html()` |
""")

# 향후 개발 계획
st.header("향후 개발 계획")
st.markdown("""
- **다양한 프로그래밍 언어 지원:** Python 외에도 JavaScript, SQL, Rust 등 다중 언어 실행 지원 예정
- **AI 모델 최적화:** Transformer 기반 모델 최적화 및 Fine-tuning 기법 활용하여 응답 속도 개선
- **사용자 코드 저장 기능:** 클라우드 기반 코드 저장 및 재실행 기능 추가
- **협업 기능 강화:** 실시간 코드 공유 및 다중 사용자 협업 환경 구축 (WebSocket 연동 예정)
""")
