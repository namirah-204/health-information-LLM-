import streamlit as st
import google.generativeai as genai
from api import api

# Configure the API key
genai.configure(api_key=api)

# Set default parameters
defaults = {
    'model': 'models/text-bison-001',
    'temperature': 0.25,
    'candidate_count': 1,
    'top_k': 40,
    'top_p': 0.95,
}

st.title('Health Information Generator')
st.write('Ask me for information about human health')
final_response = None

# Creating a side panel for inputs
with st.sidebar:
    st.write("## Health Information Generator Settings")
    # Create a text input for the health-related prompt
    health_prompt = st.text_input("What health information do you want to know?")
    # When the 'Generate' button is pressed, generate the text
    if st.button('Generate'):
        formatted_prompt = f"{health_prompt}"

        # Filter only health-related prompts
        health_keywords = ['health', 'medical', 'wellness', 'nutrition', 'fitness', 'human', 'medicine']
        if any(keyword in formatted_prompt.lower() for keyword in health_keywords):
            response = genai.chat(
                messages=formatted_prompt
            )
            final_response = response
        else:
            st.warning("Please enter a health-related prompt (e.g., health, medical, wellness, nutrition, fitness, medicine).")

if final_response is not None:
    st.write(final_response.last)