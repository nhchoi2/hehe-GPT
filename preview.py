import streamlit as st

st.title("Code Execution Preview")

# Check if generated code exists in session_state
if "generated_code" not in st.session_state or not st.session_state["generated_code"].strip():
    st.error("No generated code found. Please generate code in the main app first.")
else:
    try:
        # Execute the generated code safely
        exec(st.session_state["generated_code"], globals())
    except Exception as e:
        st.error(f"Error executing generated code: {e}")
