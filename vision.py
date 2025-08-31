from dotenv import load_dotenv
import os 
import streamlit as st
import google.generativeai as genai
import pathlib
import textwrap
from PIL import Image

if __name__ == "__main__":
    load_dotenv()
    api_key = os.getenv("GOOGLE_API_KEY")
    print(f"Your Google API Key is: {api_key}")

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")
def get_gemini_response(prompt, image=None):
    if prompt != "":
        if image is not None:
            response = model.generate_content([prompt, image])
        else:
            response = model.generate_content(prompt)
        return response.text
    return "Please enter a prompt."


## Initialize Streamlit app
st.set_page_config(page_title="Google Gemini with Streamlit", layout="wide")
st.title("Google Gemini with Streamlit")
input=st.text_input("Input:", key="input")

uploaded_file = st.file_uploader("Choose an image...",)
if uploaded_file is not None:
    # To read file as bytes:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)

submit_button = st.button("Submit")
## When user clicks submit, get response from Gemini
if submit_button:
    response=get_gemini_response(input,image)
    st.subheader("Response:")
    st.write(response)
if uploaded_file is not None:
    # To read file as bytes:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)