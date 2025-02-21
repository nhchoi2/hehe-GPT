import streamlit as st

st.title("AI가 생성한 코드 실행")

if "generated_code" in st.session_state and st.session_state["generated_code"]:
    exec(st.session_state["generated_code"])
else:
    st.warning("코드를 먼저 생성해 주세요.")
