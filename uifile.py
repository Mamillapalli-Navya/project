import streamlit as st
from code_explainer import explain_code

# Set the page configuration
# Title and description
st.set_page_config(
    page_title="Code Explainer",
    page_icon="💻",
    layout="wide"
)

st.title("Code Explainer🖥️")
st.markdown("""
New to coding?“CodeExplainer makes understanding code easy. Just drop in any code snippet, 
            and it’ll walk you through what each part does in simple terms—no jargon, no stress.”
""")
input_method = st.tabs(["Paste Code", "Upload File"])

code = ""

# Paste code
with input_method[0]:
    code = st.text_area("Paste your code here:", height=200)

code_input = st.text_area(
        label="",
        placeholder="e.g., def greet(name): return 'Hello ' + name",
        height=355,
        label_visibility="collapsed"
    )
# Upload code file
with input_method[1]:
    uploaded_file = st.file_uploader("Upload a code file", type=["py", "js", "cpp", "java", "txt"])
    if uploaded_file:
        code = uploaded_file.read().decode("utf-8")
        st.code(code, language=language.lower())

explain_button = st.button("Explain Code", type="primary")

explanation_container = st.container(height=500)
    
if explain_button and code_input:
    with st.spinner("Analyzing and explaining your code..."):
            explanation = explain_code(code_input, st.session_state.api_key)
            with explanation_container:
                st.markdown(explanation)
elif explain_button and not code_input:
        with explanation_container:
            st.error("Please enter some code to explain.")
else:
    with explanation_container:
        st.info("Enter your code and click 'Explain Code' to get an explanation.")