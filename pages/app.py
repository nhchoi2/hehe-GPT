import streamlit as st
import requests
import os

# Hugging Face API 설정
HF_API_KEY = os.getenv("HUGGINGFACE_API_KEY")  # 환경 변수에서 API 키 불러오기
MODEL_NAME = "Qwen/Qwen2.5-Coder-32B-Instruct"
API_URL = f"https://api-inference.huggingface.co/models/{MODEL_NAME}"

# API 요청 함수
def query_huggingface_api(prompt):
    headers = {"Authorization": f"Bearer {HF_API_KEY}"}
    payload = {"inputs": prompt, "parameters": {"max_length": 512, "temperature": 0.7}}

    response = requests.post(API_URL, headers=headers, json=payload)
    
    try:
        result = response.json()
        if isinstance(result, list) and "generated_text" in result[0]:
            return result[0]["generated_text"]
        else:
            return "API 응답 오류: 유효한 코드가 생성되지 않았습니다."
    except:
        return "API 응답 오류: JSON 디코딩 실패"

# 세션 상태 초기화 (없으면 빈 문자열로 설정)
if "generated_code" not in st.session_state:
    st.session_state["generated_code"] = ""

st.title("AI 코드 생성 및 실행 (Qwen API)")

# 사용자가 원하는 기능 입력
user_input = st.text_area("원하는 UI 설명을 입력하세요", "버튼과 입력창이 있는 화면을 만들어줘")

if st.button("코드 생성"):
    with st.spinner("AI가 코드를 생성하는 중..."):
        # AI에게 Streamlit 코드 생성을 요청하는 프롬프트
        prompt = f"Streamlit을 사용하여 {user_input} 기능을 구현하는 Python 코드를 작성해줘."
        response_text = query_huggingface_api(prompt)

        # API 응답에서 코드 블록만 추출
        if "```python" in response_text:
            code = response_text.split("```python")[1].split("```")[0].strip()
        else:
            code = response_text  # 코드 블록이 없으면 그대로 사용

        # 생성된 코드 저장
        st.session_state["generated_code"] = code
        st.code(code, language="python")

if "generated_code" in st.session_state and st.session_state["generated_code"]:
    if st.button("뷰 보기 (새 창)"):
        st.switch_page("pages/preview.py")