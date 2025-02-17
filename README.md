# 💬 헷GPT (HetGPT)

헷GPT는 고객 상담 및 AI 기반 대화를 지원하는 맞춤형 챗봇입니다.
Hugging Face의 **Gemma 2 모델**을 활용하여 자연어 처리를 수행하며, Streamlit을 기반으로 웹 UI를 제공합니다.

---

## 🚀 주요 기능
- **AI 기반 고객 상담**: 사용자의 질문을 분석하고 적절한 답변을 제공
- **실시간 응답**: 질문 입력 후 빠르게 AI가 응답 생성
- **대화 기록 유지**: 사용자의 대화 내용을 저장하여 지속적인 대화 가능
- **대화 기록 초기화 기능**: 필요할 때 대화 기록을 삭제 가능
- **보안 강화**: API 키를 `.env` 파일을 통해 보호

---

## 🛠️ 사용 기술
- **Hugging Face API (`google/gemma-2-9b-it` 모델 사용)**
- **Streamlit을 활용한 웹 기반 UI**
- **Python 및 NLP 기반 자연어 처리**

---

## 🔒 보안 및 데이터 보호
- **환경 변수 (`.env`) 사용** → API 키 및 민감한 정보 보호
- **`.gitignore` 설정** → `.env` 파일이 GitHub에 업로드되지 않도록 방지
- **Streamlit Cloud `Secrets Manager` 활용** → 안전한 API 키 관리
- **HTTPS 통신 사용** → 네트워크 상에서 데이터 암호화
- **대화 기록 관리** → `session_state`를 활용하여 사용자 데이터 보호

---

## 📌 인공지능 모델 출처
- 본 AI 챗봇은 **Hugging Face의 `google/gemma-2-9b-it` 모델**을 사용합니다.
- 해당 모델은 **Google이 개발한 `Gemma 2` 시리즈의 일부로**, 다양한 자연어 처리(NLP) 작업을 수행할 수 있도록 설계되었습니다.
- 모델 출처: [Hugging Face 모델 페이지](https://huggingface.co/google/gemma-2-9b-it)

---

## 📖 사용 방법
1. **앱 실행:**
   ```bash
   streamlit run customer_support_ai.py
   ```
2. **질문 입력:**
   - 입력창에 질문을 입력하면 AI가 자동으로 응답 생성
3. **대화 기록 유지:**
   - 이전 대화 내용을 저장하여 지속적인 대화 가능
4. **대화 기록 초기화:**
   - 사이드바에서 "대화 기록 초기화" 버튼을 클릭하면 대화 내역 삭제 가능

---

## 📂 프로젝트 구조
```
/hehe-GPT
 ├── customer_support_ai.py  # 메인 챗봇 코드
 ├── pages/
 │   ├── about.py  # 앱 소개 페이지
 ├── .env  # API 키 환경 변수 (Git 업로드 제외)
 ├── README.md  # 프로젝트 설명 문서
 ├── requirements.txt  # 필요한 패키지 목록
```

---

## 📩 문의 및 피드백
이 프로젝트에 대한 피드백이 있거나 개선 사항이 필요하다면 언제든지 연락 주세요! 🚀

