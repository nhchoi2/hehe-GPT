import streamlit as st  # 웹 UI 생성을 위한 Streamlit 라이브러리 임포트
from huggingface_hub import InferenceClient  # Hugging Face Inference API 사용을 위한 클라이언트 임포트
import os  # 운영체제 관련 기능 사용 (환경 변수 로드 등)
from dotenv import load_dotenv  # .env 파일에서 환경 변수를 불러오기 위한 라이브러리


# 환경 변수 로드
load_dotenv()  # .env 파일에서 환경 변수들을 불러옵니다.
api_key = os.getenv("HUGGINGFACE_API_KEY")  # 환경 변수에서 HUGGINGFACE_API_KEY 값을 가져옵니다.


# 인터넷창 열면 표시되는 이미지 및 이름 (탭이름)
st.set_page_config(
    page_title="코드헷GPT",  # 브라우저 탭에 표시될 페이지 제목 설정
    page_icon="🤖",  # 페이지 아이콘 설정 (이모지 사용 가능)
    layout="wide"  # 페이지 레이아웃을 와이드 모드로 설정하여 넓게 사용
)

# 페이지 제목 및 설명 표시
st.title("🤖 코드헷GPT")  
st.write("코드를 입력하면 헷GPT가 개선점, 디버깅 방법 등을 안내해드립니다!")  
with st.expander("**어떤 질문을 할 수 있나요?**"):
    st.markdown('''
✅ **Python 코드 최적화 방법**  
✅ **디버깅 및 오류 해결 방법**  
✅ **알고리즘 성능 개선**  
✅ **리팩토링 및 코드 스타일 가이드 적용**  
✅ **특정 라이브러리 또는 프레임워크 사용법**  

🔹 **샘플 질문 예시**
- "아래 코드에서 성능을 개선할 방법이 있을까요?"
- "이 Python 코드의 오류를 찾아주세요."
- "이 코드에서 메모리 사용량을 줄이는 방법이 있을까요?"
- "Django에서 REST API를 구현하는 방법을 알려주세요."
- "Pandas를 사용하여 데이터프레임을 빠르게 필터링하는 방법은?"

🔹 **검증용 샘플 코드**
```python
# ✅ 개선 가능성이 있는 코드 (비효율적인 리스트 순회)
numbers = [i for i in range(100000)]
squared_numbers = []
for num in numbers:
    squared_numbers.append(num ** 2)

print(sum(squared_numbers)''')


# Hugging Face InferenceClient 초기화
client = InferenceClient(provider="hf-inference", api_key=api_key)  # API 키를 사용해 Hugging Face Inference Client 생성

# 현재 페이지에 대한 고유한 키 생성 (페이지별 대화 기록 유지)
current_page = "ai_coding_assistant"  # 현재 페이지의 고유한 식별자
page_key = f"chat_history_{current_page}"

# 페이지별 대화 기록 초기화
if page_key not in st.session_state:
    st.session_state[page_key] = []

# 사이드바 초기화 버튼
if st.sidebar.button("대화 기록 초기화"):
    # 만약 사이드바의 '대화 기록 초기화' 버튼을 누르면
    st.session_state[page_key]= []  # 세션 상태에서 'chat_history' 변수를 빈 리스트로 초기화하여 대화 기록 삭제


# 기존 대화 기록 출력
for chat in st.session_state[page_key]:
    if chat["role"] == "user":
        st.chat_message("user").write(chat["content"])  
    else:
        st.chat_message("assistant").write(chat["content"])

# 사용자 입력 받기 (대화형 입력창)
user_input = st.chat_input("코드를 입력하세요:")  # 사용자가 코드를 입력할 수 있는 대화형 입력창 제공


# 사용자 입력 처리 및 AI 응답 생성
if user_input:
    # 사용자가 입력한 내용을 chat_history에 추가하고 UI에 표시
    st.session_state[page_key].append({"role": "user", "content": "한국어로 알려주세요 "+user_input})  # 사용자 입력을 기록
    st.chat_message("user").write(user_input)  # UI에 사용자 입력 표시

    # AI 응답 생성 요청: 지금까지의 대화 기록을 전달하여 문맥 기반 응답을 생성
    with st.spinner("헷GPT가 응답을 생성 중입니다..."):
        response = client.chat.completions.create(
            model="Qwen/Qwen2.5-Coder-32B-Instruct",  # 코드 관련 질문에 특화된 AI 모델 사용
            messages=st.session_state[page_key],  # 현재까지의 대화 기록을 API에 전달
            max_tokens=1024,  # 최대 응답 길이를 1024 토큰으로 제한하여 효율적인 응답 생성
        )
        assistant_message = response.choices[0].message.content  # AI 응답에서 메시지 내용 추출

    # 생성된 AI 응답을 대화 기록에 추가하고 UI에 표시
    st.session_state[page_key].append({"role": "assistant", "content": assistant_message})  # AI 응답을 기록
    st.chat_message("assistant").write(assistant_message)  # AI의 응답을 UI에 표시
