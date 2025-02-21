import streamlit as st

st.title("AI가 생성한 코드 실행")

# 코드 실행 오류 방지 처리
try:
    if "generated_code" in st.session_state and st.session_state["generated_code"]:
        exec(st.session_state["generated_code"])
    else:
        st.warning("코드를 먼저 생성해 주세요.")
except Exception as e:
    st.error(f"코드 실행 중 오류 발생: {e}")
    st.write("디버깅: 오류 메시지", str(e))
