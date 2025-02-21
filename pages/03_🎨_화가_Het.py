import streamlit as st  # Streamlit 라이브러리 임포트 (웹 UI 생성)
from huggingface_hub import InferenceClient  # Hugging Face Inference API 사용
from PIL import Image  # 이미지 처리를 위한 라이브러리
import io  # 바이트 데이터를 이미지로 변환
import os  # 환경 변수 로드를 위한 라이브러리
from dotenv import load_dotenv  # .env 파일에서 환경 변수를 로드하기 위한 라이브러리

# 환경 변수 로드
load_dotenv()  # .env 파일에서 환경 변수 불러오기
api_key = os.getenv("HUGGINGFACE_API_KEY")  # 환경 변수에서 API 키 가져오기

# Streamlit 페이지 설정
st.set_page_config(page_title="화가 헷GPT", page_icon="🎨", layout="wide")


# 웹 페이지 제목 및 설명 추가
st.title("🎨 이미지 생성하는 헷GPT")
st.write("텍스트를 입력하면 헷GPT가 이미지를 생성해줍니다!")

# Hugging Face Inference API 설정
client = InferenceClient(provider="hf-inference", api_key=api_key)  # API 키를 사용하여 Inference Client 설정

# 사용자 입력 받기 (챗 인풋으로 변경)
prompt = st.chat_input("생성할 이미지 설명을 입력하세요:")  # 사용자가 입력하는 프롬프트

# 텍스트 번역 및 변환 모델 추가 (한글 → 영어 변환 후 전달)
def translate_text(input_text):
    messages = [{"role": "user", "content": f"Translate this to English: {input_text}",}]
    completion = client.chat.completions.create(
        model="google/gemma-2-9b-it",  # 한글을 영어로 번역할 모델 사용
        messages=messages, 
        max_tokens=1024,
    )
    return completion.choices[0].message.content  # 변환된 영어 텍스트 반환

# 버튼 없이 챗 인풋 입력 시 자동 실행
if prompt:
    with st.spinner("헷GPT가 이미지를 생성 중입니다..."):
        translated_prompt = translate_text(prompt)
        # 반환값은 이미 PIL 이미지 객체임
        image = client.text_to_image(translated_prompt, model="black-forest-labs/FLUX.1-dev")
        st.image(image, caption="생성된 이미지", use_container_width=True)
