import streamlit as st

# 페이지 설정
st.set_page_config(page_title="헷GPT 소개", layout="wide")

# 제목
st.title("헷GPT: 실시간 코드 실행 및 AI 챗봇")

# 개요
st.header("개요")
st.write(
    "헷GPT는 Python 및 HTML 코드를 실행하고, AI 챗봇과 대화할 수 있는 웹 애플리케이션입니다. "
    "또한, Hugging Face의 AI 모델을 활용하여 다양한 기능을 제공합니다. "
    "개발자, 학생, 연구자 등 누구나 쉽게 사용할 수 있도록 설계되었습니다."
)

# 주요 기능
st.header("주요 기능")
st.markdown("""
- **Python 코드 실행:** 사용자가 입력한 Python 코드를 서버에서 안전하게 실행하고 결과를 출력
- **HTML 코드 미리보기:** HTML 코드를 직접 입력하고, 렌더링된 웹 페이지를 실시간으로 미리보기
- **AI 챗봇:** Hugging Face의 AI 모델을 활용한 대화형 챗봇 (잼마 모델 사용)
- **Qwen 모델 기반 코드 생성:** Qwen AI 모델을 활용한 코드 생성 및 코드 지원 기능 제공
- **AI 이미지 생성:** 텍스트를 입력하면 AI가 이미지를 생성
- **보안 강화:** `.env` 파일을 사용하여 API 키 보호 및 Streamlit Secrets 설정
- **자동 배포:** GitHub Actions를 이용하여 Streamlit Cloud에 자동 배포
""")

# 사용된 인공지능 모델
st.header("사용된 AI 모델")
st.markdown("""
- **잼마 모델 (`google/gemma-2-9b-it`)** → 헷GPT 챗봇에 사용
- **Qwen 모델 (`Qwen/Qwen2.5-Coder-32B-Instruct`)** → 코드 생성 및 개발 보조 기능에 사용
- **FLUX 모델 (`black-forest-labs/FLUX.1-dev`)** → AI 이미지 생성에 사용
""")

# 보안 및 배포 방식
st.header("보안 및 배포")
st.markdown("""
- **환경 변수 (.env) 사용** → API 키, Hugging Face 토큰 등을 `.env` 파일에 저장하여 보안 유지
- **GitHub Secrets 사용** → GitHub Actions에서 배포 시 환경 변수 보호
- **Streamlit Secrets 사용** → 배포 환경에서 안전하게 API 키 관리
- **자동 배포 시스템** → GitHub Actions를 이용한 자동 배포 설정
""")

# 각 페이지별 기능 & 기술 설명
st.header("각 페이지별 기능 & 기술")
st.markdown("""
| 페이지명 | 설명 | 사용 기술 |
|---------|------|----------|
| **ℹ️ 헷GPT 소개** | 프로젝트 개요 및 기능 설명 | Streamlit UI |
| **🤗 헷GPT (챗봇)** | AI 챗봇 (잼마 모델 활용) | Hugging Face, `google/gemma-2-9b-it` |
| **🤖 코드 헷GPT** | AI 기반 코드 분석 & 디버깅 | Qwen AI 모델 (`Qwen2.5-Coder-32B-Instruct`) |
| **🎨 화가 헷GPT** | 텍스트 기반 AI 이미지 생성 | `black-forest-labs/FLUX.1-dev` |
| **💻 실행 헷GPT** | Python & HTML 코드 실행 | `exec()`, `streamlit.components.v1.html()` |
""")

# 향후 개발 계획
st.header("향후 개발 계획")
st.markdown("""
- **다양한 프로그래밍 언어 지원:** Python 외에도 JavaScript, SQL 등의 코드 실행 지원
- **AI 모델 확장:** 대화형 챗봇 성능 개선 및 다양한 AI 모델 추가
- **사용자 코드 저장 기능:** 작성한 코드를 저장하고 다시 실행할 수 있는 기능 추가
- **협업 기능 추가:** 실시간 코드 공유 및 다중 사용자 지원
""")
