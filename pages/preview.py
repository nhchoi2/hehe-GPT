import streamlit as st
import sys
import io

# 페이지 설정
st.set_page_config(
    page_title="Preview",
    layout="wide"
)

st.title("Python Code Execution Preview")

# --- New Feature: User Code Execution ---
st.header("💻 직접 입력한 코드 실행")

# 채팅 입력창에서 Python 코드 입력 받기
user_code = st.chat_input("실행할 Python 코드를 입력하세요:")

if user_code:
    st.write("🛠️ 실행 결과:")

    # 표준 출력을 캡처하여 실행 결과를 가져오기
    old_stdout = sys.stdout
    sys.stdout = io.StringIO()  # 새로운 출력 버퍼 설정

    try:
        exec(user_code, globals())  # 코드 실행
        output = sys.stdout.getvalue()  # 실행 결과 가져오기
        if output.strip():
            st.code(output, language="plaintext")  # 실행 결과 출력
        else:
            st.success("✅ 코드가 성공적으로 실행되었습니다. 출력 결과는 없습니다.")
    except Exception as e:
        st.error(f"❌ 코드 실행 중 오류 발생: {e}")
    finally:
        sys.stdout = old_stdout  # 원래 stdout으로 복구
