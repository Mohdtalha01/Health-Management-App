from dotenv import load_dotenv
load_dotenv()

import google.generativeai as genai
import streamlit as st
import os
from PIL import Image

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))



def get_gemini_response(input,image,prompt):
    model=genai.GenerativeModel("gemini-pro-vision")
    response=model.generate_content([input,image[0],prompt])
    return response.text


def input_image_setup(uploaded_file):
    if uploaded_file is not None:
        bytes_data=uploaded_file.getvalue()


        image_parts=[
            {
                "mime_type": uploaded_file.type,
                "data":bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No File uploaded")


#streamlit 

st.set_page_config(page_title="Health Tracker")

st.header("Health Management App")
input=st.text_input("Input Prompt: ", key="input")
uploaded_file=st.file_uploader("Choose an image...",type=["jpg","jpeg","png"])
image=""
if uploaded_file is not None:
    image=Image.open(uploaded_file)
    st.image(image,caption="Uploaded Image.",use_column_width=True)


submit=st.button("Tell me the total calories")

input_prompt="""
        you are an expert in nutritionist where you need to see the food items from the image and calculate 
        the total calories, also provide the details of eavery food items with calories intake 
        just like format given below

        1. Item 1 - No. of calories
        2. Item 2 - No. of calories
        ....
        ...

"""

if submit:
    image_data=input_image_setup(uploaded_file)
    response=get_gemini_response(input_prompt,image_data,input)
    st.subheader("The response is")
    st.write(response)