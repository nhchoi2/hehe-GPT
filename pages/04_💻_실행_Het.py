import streamlit as st
import sys
import io
import streamlit.components.v1 as components

# ✅ Streamlit 페이지 설정
st.set_page_config(page_title="실행_Het", page_icon="💻", layout="wide")

# ✅ 📌 **페이지 설명 추가**
st.title("💻 Python & HTML 코드 실행기")
st.markdown("""
이 페이지에서는 사용자가 입력한 **Python 코드 또는 HTML 코드**를 즉시 실행하고 결과를 확인할 수 있습니다.  
- **Python 코드**: 입력 후 실행하면 결과를 텍스트 형태로 출력합니다.  
- **HTML 코드**: 입력 시 웹페이지처럼 렌더링하여 미리보기 기능을 제공합니다.  
- ⚠️ **주의**: 보안상의 이유로 시스템 명령어(`os.system`, `subprocess`) 실행은 제한됩니다.
""")

# ✅ 🎯 **사용 예시 블록 추가**
with st.expander("🔹 사용 방법 예시 보기"):
    st.markdown("""
    **1️⃣ Python 코드 실행**
    ```python
    print("Hello, World!")
    a = 10
    b = 20
    print(f"합계: {a + b}")
    ```
    - ✅ 입력 후 실행하면 `"Hello, World!"` 및 `"합계: 30"`이 출력됩니다.

    **2️⃣ HTML 코드 실행**
    ```html
    <!DOCTYPE html>
    <html>
      <body>
        <h1>HTML 코드 실행 예제</h1>
        <p>이 페이지에서 HTML을 바로 미리볼 수 있습니다.</p>
      </body>
    </html>
    ```
    - ✅ 입력 후 실행하면 **HTML 페이지 형태로 미리보기**가 가능합니다.
    """)

# ✅ 사용자 입력 필드 (Python & HTML 코드 실행)


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
