# 🎯 HEHE-GPT (헷GPT) - 올인원 AI 도우미  
![Python](https://img.shields.io/badge/Python-3.9%2B-blue) ![Streamlit](https://img.shields.io/badge/Streamlit-1.0-red) ![Pinecone](https://img.shields.io/badge/Pinecone-VectorDB-green) ![HuggingFace](https://img.shields.io/badge/HuggingFace-Gemma--2--9b--it-orange)

HEHE-GPT(헷GPT)는 **AI 검색, 실시간 코드 실행, AI 이미지 생성, 세금 계산 (RAG)기능을 사용한 올인원 개발 도우미**입니다.  
Python 및 Streamlit 기반으로 구현되어있으며, **Pinecone 베터 검색** 및 **Hugging Face AI 모델**을 활용하여 **강강력한 AI 경험을 제공합니다.**

---

## 📌 **프로젝트 개요**
👉 **AI 기반 개발 보조 도구:** 실시간 코드 실행, AI 검색 지원  
👉 **AI 이미지 생성:** Stable Diffusion 기반 이미지 생성  
👉 **AI 코드작성** Qwen 모델 기반으로 개발보조조
👉 **세금 계산기:** 세금 관련 질문을 AI가 분석하여 가이드 제공  
👉 **Pinecone 벡터 검색:** 법령 검색을 통한 AI 검색 기능 강화  
👉 **Streamlit 기반 UI 제공**  

---

## 📚 **프로젝트 폴더 구조**
```bash
HEHE-GPT/
│ .devcontainer/           # 개발 환경 설정 폴더 (VS Code Dev Container)
│   ├ devcontainer.json    # Dev Container 설정 파일
│
│ pages/                   # Streamlit 페이지 폴더
│   ├ 01_🤗_Het_GPT.py       # AI 창보트 (Hugging Face + Pinecone)
│   ├ 02_🤖_코드_Het.py       # AI 코드 분석 (Qwen 모델 적용)
│   ├ 03_🎨_화가_Het.py       # AI 이미지 생성 (Stable Diffusion)
│   ├ 04_💻_실행_Het.py       # 실시간 코드 실행 기능
│   ├ 05_📚_세법_Het.py       # 세무 AI 검색 (법령 데이터 검색 + AI 답변)
│
│ .env                      # 환경 변수 파일 (API Key 저장)
│ .gitignore                # Git에서 제외할 파일 목록
│ README.md                 # 프로젝트 설명
│ requirements.txt          # Python 패키지 목록
│ i_헷GPT_소개.py            # 프로젝트 소개 페이지
```

---

## 🛠 **설치 방법**
### 1️⃣ **Python 환경 설정**
```bash
# 가상 환경 생성 및 활성화
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate  # Windows
```

### 2️⃣ **필수한 패키지 설치**
```bash
pip install -r requirements.txt
```

### 3️⃣ **환경 변수 설정 (.env)**
```ini
HUGGINGFACE_API_KEY=your_huggingface_api_key
PINECONE_API_KEY=your_pinecone_api_key
PINECONE_CLOUD=aws
PINECONE_ENV=us-east-1
PINECONE_INDEX_NAME=your_index_name
```

### 4️⃣ **Streamlit 앱 실행**
```bash
streamlit run i_헷GPT_소개.py
```

**브라우저에서 `https://hehe-gpt-bteegm9nujshfwm4sgxkgf.streamlit.app/`로 접속하면 헷헷GPT 사용 가능!** 🚀

