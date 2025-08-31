from dotenv import load_dotenv
import os 
import streamlit as st
import google.generativeai as genai

if __name__ == "__main__":
    load_dotenv()
    api_key = os.getenv("GOOGLE_API_KEY")
    print(f"Your Google API Key is: {api_key}")


genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


## Function to get response from Gemini
model = genai.GenerativeModel("gemini-1.5-flash")
def get_gemini_response(prompt):
    response= model.generate_content(prompt)
    return response.text


## Initialize Streamlit app
st.set_page_config(page_title="Google Gemini with Streamlit", layout="wide")
st.title("Google Gemini with Streamlit")
user_input = st.text_area("Input:", key="input", height=200)
submit_button = st.button("Submit")

## When user clicks submit, get response from Gemini
if submit_button:
    response=get_gemini_response(user_input)
    st.subheader("Response:")
    st.write(response)
