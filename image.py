from dotenv import load_dotenv
load_dotenv()  # take environment variables from .env.
import os
import streamlit as st
from PIL import Image
import google.generativeai as genai
# Example: Display a variable from your .env file
api_key = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


### Function to load gemini pro vision model

model = genai.GenerativeModel('gemini-2.5-pro')

def get_gemini_response(input,image,prompt):
    response=model.generate_content([input,image[0],prompt])
    return response.text

def input_image_setup():
    if uploaded_file is not None:
        byte_data = uploaded_file.getvalue()
        image_parts=[{
            "mime_type": uploaded_file.type,
            "image_base64": byte_data
        }]
        return image_parts
    else:
        return FileNotFoundError("No file uploaded")


## Initialize Streamlit app
st.set_page_config(page_title="Multi Language Invoice Extractor")
input = st.text_input("Input Prompt:", key="input")
uploaded_file = st.file_uploader("Choose an image of the invoice...", type=["png", "jpg", "jpeg"])
image=""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    st.write("")
    st.write("Classifying...")
submit = st.button('Submit')

input_prompt="Extract all the key information from this invoice in json format with keys as Invoice Number," \
                " Invoice Date, Due Date, Total Amount, Vendor Name, Vendor Address, Vendor Phone Number, Vendor Email, Customer Name," \
                " Customer Address, Customer Phone Number, Customer Email, Line Items (with Description, Quantity, Unit Price" \
                " and Total Price), Subtotal, Tax, Total Amount Due."
if submit:
    image_parts=input_image_setup()
    if isinstance(image_parts, FileNotFoundError):
        st.error("Please upload an image file.")
    else:
        response=get_gemini_response(input,image_parts,input_prompt)
        st.success("Response:")
        st.write(response)