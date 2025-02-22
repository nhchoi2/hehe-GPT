import streamlit as st

# 📌 페이지 설정
st.set_page_config(page_title="ℹ️ 헷GPT 소개", page_icon="ℹ️", layout="wide")

# 📌 CSS 적용 (모던 카드 UI)
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
    </style>
""", unsafe_allow_html=True)

# 📌 ℹ️ 헷GPT 소개 페이지 제목
st.markdown('<div class="card">', unsafe_allow_html=True)
st.title("ℹ️ 헷GPT - AI 기반 개발 도우미")
st.subheader("Python & AI를 활용한 차세대 개발 및 학습 도구")
st.write("""
헷GPT는 **AI 챗봇, 코드 실행, AI 이미지 생성, 세무 상담** 기능을 통합한 웹 애플리케이션입니다.  
Hugging Face AI 모델과 Pinecone 벡터 검색을 활용하여 **개발자, 데이터 사이언티스트, 연구자** 등 누구나 쉽게 활용할 수 있도록 설계되었습니다.
""")
st.markdown('</div>', unsafe_allow_html=True)

# 📌 🌟 주요 기능 - 탭 기능 추가
tab1, tab2, tab3, tab4 = st.tabs(["🎯 주요 기능", "🤖 AI 모델", "🔒 보안 & 배포", "🚀 향후 개발 계획"])

with tab1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("🎯 주요 기능")
    st.markdown("""
    - **💬 AI 챗봇** → Gemma-2-9B-it 기반 대화형 AI  
    - **📝 Python 코드 실행** → 코드 실행 및 디버깅 지원  
    - **🎨 AI 이미지 생성** → Stable Diffusion을 활용한 이미지 생성  
    - **📜 세무법령 상담** → Pinecone 벡터 검색을 활용한 세무 Q&A  
    - **🔍 AI 코드 분석** → Qwen 모델 기반 코드 최적화 및 리팩토링  
    """)
    st.markdown('</div>', unsafe_allow_html=True)

with tab2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("🤖 사용된 AI 모델")
    st.markdown("""
    - **Gemma-2-9B-it** → 자연어 처리 & AI 챗봇  
    - **Qwen-2.5-Coder-32B** → AI 코드 분석 및 리팩토링  
    - **Stable Diffusion (FLUX)** → AI 이미지 생성  
    """)
    st.markdown('</div>', unsafe_allow_html=True)

with tab3:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("🔒 보안 및 배포")
    st.markdown("""
    - **환경 변수 (.env) 사용** → API 키 보호  
    - **Streamlit Secrets 적용** → 안전한 클라이언트 인증  
    - **Streamlit Cloud 무료 배포** → 빠르고 가벼운 서비스  
    """)
    st.markdown('</div>', unsafe_allow_html=True)

with tab4:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("🚀 향후 개발 계획")
    st.markdown("""
    - **💡 다중 프로그래밍 언어 지원** → JavaScript, SQL 등 추가  
    - **⚡ AI 모델 최적화** → Transformer 기반 Fine-tuning  
    - **☁️ 사용자 코드 저장 기능** → 클라우드 연동  
    - **👥 실시간 협업 지원** → 코드 공유 및 협업 기능  
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# 📌 🔗 기능별 바로 가기 버튼 추가
st.markdown('<div class="card">', unsafe_allow_html=True)
st.subheader("🔗 각 기능 페이지 바로 가기")
st.write("각 기능별 페이지를 클릭하여 직접 사용해보세요!")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.button("🤗 헷GPT (챗봇 페이지)", key="chatbot")

with col2:
    st.button("🤖 코드 헷GPT (AI 코드 분석)", key="code_helper")

with col3:
    st.button("🎨 화가 헷GPT (AI 이미지 생성)", key="image_gen")

with col4:
    st.button("💻 실행 헷GPT (코드 실행)", key="code_execution")

st.markdown('</div>', unsafe_allow_html=True)
