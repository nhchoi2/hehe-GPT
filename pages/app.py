import streamlit as st
import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env (ensure you have HF_API_KEY set)
load_dotenv()

st.title("Streamlit Code Generator")
st.write("Enter a description of the UI functionality you want, and an AI model will generate the corresponding Streamlit code.")

# Text area for UI description
user_description = st.text_area("UI Description", height=150)

# When "Generate Code" is clicked, trigger the API request
if st.button("Generate Code"):
    if not user_description.strip():
        st.error("Please enter a UI description!")
    else:
        try:
            st.info("Generating code, please wait...")
            api_key = os.getenv("HUGGINGFACE_API_KEY")
            if not api_key:
                st.error("API key not found. Please set HF_API_KEY in your .env file.")
            headers = {"Authorization": f"Bearer {api_key}"}
            payload = {
                "inputs": f"Generate Streamlit code for the following UI description:\n\n{user_description}\n",
                "parameters": {"max_new_tokens": 512},
                "options": {"wait_for_model": True}
            }
            # Call the Hugging Face Inference API
            response = requests.post(
                "https://api-inference.huggingface.co/models/Qwen/Qwen2.5-Coder-32B-Instruct",
                headers=headers,
                json=payload
            )
            if response.status_code != 200:
                st.error(f"Error generating code: {response.status_code} - {response.text}")
            else:
                result = response.json()
                # Parse the result depending on the API response structure.
                if isinstance(result, list) and "generated_text" in result[0]:
                    generated_code = result[0]["generated_text"]
                else:
                    generated_code = result.get("generated_text", "")
                if not generated_code:
                    st.error("No code was generated. Please try again with a different description.")
                else:
                    st.session_state["generated_code"] = generated_code
                    st.success("Code generated successfully!")
        except Exception as e:
            st.error(f"An error occurred: {e}")

# Display the generated code (if available)
if "generated_code" in st.session_state and st.session_state["generated_code"].strip():
    st.subheader("Generated Code Preview")
    st.code(st.session_state["generated_code"], language="python")
    
    # Provide a link to view the preview page
    st.markdown(
        f'<a href="../preview" target="_blank"><button style="padding:10px 20px; font-size:16px;">뷰 보기 (새 창)</button></a>',
        unsafe_allow_html=True
    )
