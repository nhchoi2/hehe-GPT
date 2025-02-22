import streamlit as st

# 📌 페이지 설정
st.set_page_config(page_title="💻 실행_Het", page_icon="💻", layout="wide")

# 📌 CSS 적용 (모던 카드 스타일)
st.markdown("""
    <style>
        body {
            background-color: #f8f9fa;
            font-family: 'Poppins', sans-serif;
        }
        .card {
            background: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
            margin-bottom: 20px;
        }
        .stButton > button {
            background: linear-gradient(135deg, #6e8efb, #a777e3);
            color: white;
            font-size: 16px;
            border-radius: 10px;
            padding: 10px;
            transition: 0.3s;
        }
        .stButton > button:hover {
            transform: scale(1.05);
        }
        .stTextInput > div, .stTextArea > div {
            border-radius: 10px;
            box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.1);
        }
    </style>
""", unsafe_allow_html=True)

# 📌 💻 실행_Het 페이지 설명 추가
st.markdown('<div class="card">', unsafe_allow_html=True)
st.title("💻 실행_Het - Python & HTML 코드 실행기")
st.markdown("""
이 페이지에서는 **사용자가 입력한 Python 또는 HTML 코드**를 실행하고 결과를 확인할 수 있습니다.  
- **Python 코드**: 입력 후 실행하면 결과를 출력합니다.  
- **HTML 코드**: 입력 후 웹페이지처럼 미리보기를 제공합니다.  
- ⚠️ **보안상의 이유로 시스템 명령어 (`os.system`, `subprocess`) 실행은 제한됩니다.**
""")
st.markdown('</div>', unsafe_allow_html=True)

# 📌 사용법 샘플 (접기/펼치기 기능 추가)
with st.expander("💡 사용방법 & 샘플 코드 확인"):
    st.markdown("""
    **1️⃣ Python 코드 실행 샘플**
    ```python
    print("Hello, World!")
    a = 10
    b = 20
    print(f"합계: {a + b}")
    ```
    **2️⃣ HTML 코드 실행 샘플**
    ```html
    <!DOCTYPE html>
    <html>
      <body>
        <h1>HTML 코드 실행 예제</h1>
        <p>이 페이지에서 HTML을 바로 미리볼 수 있습니다.</p>
      </body>
    </html>
    ```
    - ✅ Python 코드는 실행하면 결과가 출력됩니다.
    - ✅ HTML 코드는 실행 후 **웹페이지 형태로 미리보기 가능**합니다.
    """)

# 📌 사용자 입력 필드 (st.chat_input() 활용)
st.markdown('<div class="card">', unsafe_allow_html=True)
code_input = st.chat_input("Python 또는 HTML 코드를 입력하세요...", key="code_chat_input")
st.markdown('</div>', unsafe_allow_html=True)

# 📌 코드 실행 처리 함수
def execute_code():
    if not code_input:
        return
    
    st.markdown('<div class="card">', unsafe_allow_html=True)
    
    if code_input.strip().startswith("<"):
        # **HTML 코드 실행 (미리보기)**
        st.subheader("📜 HTML 실행 결과:")
        st.components.v1.html(code_input, height=300)
    else:
        # **Python 코드 실행 (결과 출력)**
        try:
            exec_globals = {}
            exec(code_input, exec_globals)
            st.subheader("📌 Python 실행 결과:")
            st.write(exec_globals)
        except Exception as e:
            st.error(f"❌ 실행 중 오류 발생: {e}")
    
    st.markdown('</div>', unsafe_allow_html=True)

# 📌 사용자가 입력 후 실행하도록 설정
if code_input:
    execute_code()


