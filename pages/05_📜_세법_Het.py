import streamlit as st
from huggingface_hub import InferenceClient
from dotenv import load_dotenv
import os
from pinecone import Pinecone, ServerlessSpec

# 1. 환경 변수 로드 (.env 파일)
load_dotenv()
api_key = os.getenv("HUGGINGFACE_API_KEY")
pinecone_api_key = os.getenv("PINECONE_API_KEY")
pinecone_env = os.getenv("PINECONE_ENV")
pinecone_index_name = os.getenv("PINECONE_INDEX_NAME")
pinecone_cloud = os.getenv("PINECONE_CLOUD")  # 예: 'aws'

# 2. Hugging Face API 클라이언트 초기화
# - 채팅 응답용: google/gemma-2-9b-it 모델
client = InferenceClient(provider="hf-inference", api_key=api_key)
# - 임베딩 생성용: sentence-transformers/all-MiniLM-L6-v2 모델
embedding_client = InferenceClient(model="sentence-transformers/all-MiniLM-L6-v2", api_key=api_key)

# 3. Pinecone 인스턴스 생성 (최신 인터페이스 사용)
pc = Pinecone(api_key=pinecone_api_key)
# Pinecone 인덱스가 존재하는지 확인하고, 없으면 생성 (all-MiniLM-L6-v2 임베딩 차원은 384)
if pinecone_index_name not in [idx.name for idx in pc.list_indexes()]:
    pc.create_index(
        name=pinecone_index_name,
        dimension=384,
        metric='cosine',
        spec=ServerlessSpec(cloud=pinecone_cloud, region=pinecone_env)
    )
# 인덱스 연결
index = pc.Index(pinecone_index_name)

# 4. Streamlit UI 설정
st.set_page_config(page_title="📜_세법_Het", page_icon="💬", layout="wide")

current_page = "ai_tex_assistant"  # 현재 페이지의 고유한 식별자
page_key = f"chat_history_{current_page}"

# 페이지별 대화 기록 초기화
if page_key not in st.session_state:
    st.session_state[page_key] = []

# 사이드바: 설정 및 대화 기록 초기화
with st.sidebar:
    st.header("📌 설정")
    clear_chat = st.button("💬 대화 기록 초기화")
    if clear_chat:
        st.session_state[page_key] = []
        st.success("대화 기록이 초기화되었습니다.")

# 메인 타이틀 및 설명
st.title("📜_세법_Het")
st.write("질문을 입력하면 📜_세법_Het이 답변해드립니다.")
with st.expander("🔹 사용 방법 예시 보기"):
    st.markdown("""
이 페이지는 **세무법령에 대한 AI 챗봇**입니다.  
사용자가 입력한 질문을 **AI가 분석하여 적절한 세무 정보를 제공**합니다.  
- 🔍 **Pinecone 데이터베이스**를 활용하여 관련 법령을 검색  
- 🤖 **Hugging Face AI 모델(Gemma-2-9B-it)**이 법령을 분석하여 자연스러운 답변 제공  

📌 **어떤 질문을 할 수 있나요?**

✅ 소득세, 법인세, 부가가치세 관련 법령  
✅ 세무 감면 및 공제 혜택  
✅ 사업자 세금 신고 절차  
✅ 종합소득세 신고 기한 및 제출 방법
✅ 기타 세무 관련 법령 및 절차  

⚠️ **주의:** AI가 제공하는 정보는 참고용이며, 실제 법률 자문이 필요할 경우 전문가와 상담하세요.
""")
def get_embedding(text):
    result = embedding_client.feature_extraction(text)
    # 만약 결과가 numpy ndarray라면 리스트로 변환합니다.
    if hasattr(result, "tolist"):
        result = result.tolist()
    # 만약 다중 토큰 임베딩 리스트라면, 첫 번째 토큰의 임베딩을 사용합니다.
    if isinstance(result, list) and isinstance(result[0], list):
        return result[0]
    return result

def query_pinecone(query_text, top_k=3):
    embedding = get_embedding(query_text)
    if embedding is None:
        return None
    results = index.query(vector=embedding, top_k=top_k, include_metadata=True)
    return results

def generate_prompt(user_input, context):
    system_prompt = """
        당신은 전문적인 세무사 관리자입니다. 항상 친절하고 자세하게 답변하세요.
        사용자가 질문을 입력하면, 해당 질문에 대해 전문적인 세무 상담 답변을 제공합니다.

        - 질문이 너무 짧거나 구체적인 내용이 부족하면 반드시 "질문에 대한 내용이 많아 답변이 어렵습니다. 구체적으로 질문해주세요"라는 메시지로 응답하십시오.
        - Pinecone에서 적절한 답변을 찾을 수 없는 경우, 잼마 모델의 LLM을 활용하여 답변을 생성하십시오.
        - 사용자가 세무사 추천을 요청하는 경우, 다음 정보를 제공하십시오:

        **추천 세무사**  
        - **권도윤 세무사**  
        - **THE KEVIN's TAX LAB**  
        - **전화: 02-403-0601**
        """
    # 사용자 질문이 너무 짧은 경우 바로 해당 메시지를 반환합니다.
    if len(user_input.strip()) < 10:
        return "세법 관련 내용만 답변이 가능 합니다. "
    
    prompt = f"{system_prompt}\nContext:\n{context}\n\nQuestion: {user_input}\nAnswer:"
    return prompt

def get_response():
    user_input = st.session_state.chat_input
    if user_input:
        with st.spinner("세법_Het이 답변을 생성 중입니다..."):
            # Pinecone에서 관련 컨텍스트 검색
            results = query_pinecone(user_input)
            context = ""
            if results and "matches" in results:
                for match in results["matches"]:
                    context += match["metadata"].get("text", "") + "\n"
            
            # 기존 대화 기록을 하나의 문자열로 합치기
            conversation_history = ""
            for role, message in st.session_state[page_key]:
                conversation_history += f"{role} {message}\n"
            
            # 프롬프트 생성 시 대화 기록을 포함
            system_prompt = """
                당신은 전문적인 한국인 세무사 관리자입니다. 항상 친절하고 자세하게 답변하세요.
                사용자가 질문을 입력하면, 해당 질문에 대해 전문적인 세무 상담 답변을 제공합니다.
                ...
            """
            # 전체 프롬프트 구성
            prompt = f"{system_prompt}\n대화 기록:\n{conversation_history}\nContext:\n{context}\n\n사용자: {user_input}\n모델:"
            
            # 프롬프트가 단순한 구체성 부족 메시지인 경우, 모델 호출 없이 해당 메시지를 응답으로 사용
            if user_input.strip() == "":
                response = "질문에 대한 내용이 많아 답변이 어렵습니다. 구체적으로 질문해주세요."
            else:
                response = client.chat.completions.create(
                    model="google/gemma-2-9b-it",
                    messages=[{"role": "user", "content": prompt}],
                    max_tokens=1024,
                ).choices[0].message.content
            
            # 대화 기록 업데이트 (최신 메시지가 위에 표시되도록)
            st.session_state[page_key] .insert(0, ("👤 사용자:", user_input))
            st.session_state[page_key] .insert(0, ("🤖 세법_Het:", response))
            st.session_state.pop("chat_input", None)

# 대화 기록 출력 (최신 메시지가 위쪽에 보이도록 역순 출력)
st.markdown("### 대화 기록")
for role, message in reversed(st.session_state[page_key]):
    st.markdown(f"**{role}** {message}")

# 채팅 입력 필드: 입력 후 get_response 함수 호출
st.chat_input("질문을 입력하세요:", key="chat_input", on_submit=get_response)
