import streamlit as st
from langchain.chains import LLMChain
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
import os

# Initialize session state for API key if it doesn't exist
if 'api_key' not in st.session_state:
    st.session_state.api_key = "AIzaSyDM1mrF8SEc-iULF2iFeixNiHJzwV28R9o"


# Main function to explain code using LangChain and Claude
def explain_code(code, api_key, level_of_detail="detailed"):
    # Make sure API key is provided
    if not api_key:
        return "Please enter your Google API Key in the sidebar."
    
    # Set API key
    os.environ["GOOGLE_API_KEY"] = api_key
    
    # Initialize the Gemini model
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")
    
    # Create prompt template
    prompt_template = PromptTemplate(
        input_variables=["code", "level_of_detail"],
        template="""
        You are an expert code explainer. Your task is to explain the following code in a {level_of_detail} way.
        
        CODE:
        ```
        {code}
        ```
    
    ("system", 
You are an expert code reviewer and technical educator.
Given the following code snippet, provide a comprehensive, step-by-step explanation suitable for a developer who wants to deeply understand and learn from the code.

Please include:

overview – What the code accomplishes.

Detailed walkthrough – Break down each function or block.

Key variables and data structures – What they represent and how they interact.

Algorithms or design patterns used – Highlight anything noteworthy.

Edge cases or bugs – What might go wrong and why.

Integration logic – How the parts come together.
"""
    )
    
    # Create the chain
    chain = LLMChain(llm=llm, prompt=prompt_template)
    
    try:
        # Run the chain
        result = chain.run(code=code, level_of_detail=level_of_detail)
        return result
    except Exception as e:
        return f"Error: {str(e)}"