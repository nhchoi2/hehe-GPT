import streamlit as st
import sys
import io
import streamlit.components.v1 as components

# 페이지 설정
st.set_page_config(
    page_title="Preview",
    layout="wide"
)

st.title("Python Code Execution Preview")
st.header("💻 직접 입력한 코드 실행")

# 사용자 입력창 (Python 코드 또는 HTML 코드 입력)
user_code = st.chat_input("실행할 코드를 입력하세요:")

if user_code:
    st.write("🛠️ 실행 결과:")

    # 입력된 코드가 HTML 코드로 보이는 경우
    if user_code.strip().lower().startswith("<!doctype html>") or user_code.strip().lower().startswith("<html"):
        try:
            # HTML 코드를 렌더링 (높이는 필요에 따라 조정)
            components.html(user_code, height=600)
        except Exception as e:
            st.error(f"HTML 렌더링 중 오류 발생: {e}")
    else:
        # Python 코드 실행을 위한 표준 출력 캡처
        old_stdout = sys.stdout
        sys.stdout = io.StringIO()
        try:
            exec(user_code, globals())  # Python 코드 실행
            output = sys.stdout.getvalue()  # 실행 결과 캡처
            if output.strip():
                st.code(output, language="plaintext")
            else:
                st.success("✅ 코드가 성공적으로 실행되었습니다. 출력 결과는 없습니다.")
        except Exception as e:
            st.error(f"❌ 코드 실행 중 오류 발생: {e}")
        finally:
            sys.stdout = old_stdout  # 원래 stdout 복원
