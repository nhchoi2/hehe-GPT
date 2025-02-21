import streamlit as st
import os

# 세션 상태 초기화
if "generated_code" not in st.session_state:
    st.session_state["generated_code"] = ""

st.title("AI 코드 생성 및 실행 (Qwen API)")

user_input = st.text_area("원하는 UI 설명을 입력하세요", "버튼과 입력창이 있는 화면을 만들어줘")

if st.button("코드 생성"):
    # AI 모델이 생성한 예제 코드 (실제 API 연동 가능)
    generated_code = f"""
import streamlit as st

st.title("하이미디어")

st.subheader("현재 숫자:")
if "count" not in st.session_state:
    st.session_state.count = 0

st.markdown(f"<h1 style='text-align: center;'>{st.session_state.count}</h1>", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    if st.button("증가"):
        st.session_state.count += 1
        st.rerun()
with col2:
    if st.button("감소"):
        st.session_state.count -= 1
        st.rerun()
    """

    # 생성된 코드 저장
    st.session_state["generated_code"] = generated_code
    st.code(generated_code, language="python")

# 새 창에서 실행 버튼
if "generated_code" in st.session_state and st.session_state["generated_code"]:
    st.markdown(
        f'<a href="preview" target="_blank"><button style="padding:10px 20px; font-size:16px;">뷰 보기 (새 창)</button></a>',
        unsafe_allow_html=True
    )
