from dotenv import load_dotenv
import os 
import streamlit as st

load_dotenv()
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function to get response from Gemini
model = genai.GenerativeModel("gemini-1.5-flash")
chat= model.start_chat(history=[])

def get_gemini_response(prompt):
    response= chat.send_message(prompt,stream=True)
    return response

## Initialize Streamlit app
st.set_page_config(page_title="Google Gemini Chat with Streamlit")
st.header("Google Gemini Chat with Streamlit")

if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []


input=st.text_input("Input:", key="input")
submit_button = st.button("Ask the questions")

if submit_button and input:
    response= get_gemini_response(input)
    ## Add user query and response to session chat history
    st.session_state['chat_history'].append(("User", input))
    st.subheader("Response:")
    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append("Bot",chunk.text)
st.subheader("Chat History:")


for role,text in st.session_state['chat_history']:
    st.write(f"{role}: {text}")