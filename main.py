import streamlit as st
from streamlit_chat import message
from bardapi import Bard
import os

os.environ['_BARD_API_KEY'] = "ZwgvfP37iHbsWxdcX1blTpP-bds7wjQRympBGfidWTmc4VQe4B5I82_qqSvz_KihLfaxiQ."

# set your __Secure-1PSID value to key

st.set_page_config(page_title="Personal AI Chatbot")
st.markdown(
    '''
    <style>
        [data-testid="stAppViewContainer"] {
            background-image: url("https://c4.wallpaperflare.com/wallpaper/306/908/890/spots-background-light-dark-wallpaper-preview.jpg");
            background-size: cover;
        }
        .body {
            background-color: rgba(0, 0, 0, 0) !important;
        }
    </style>
    ''',
    unsafe_allow_html=True,
)

st.title("Your Personal AI Chatbot!")


# Function to generate a response
def generate_response(prompt):
    # set your input text
    input_text = prompt

    # Send an API request and get a response.
    response = Bard().get_answer(prompt)['content']
    return response


def get_text():
    input_text = st.text_input("Made by Shreshth Maurya, NSUT", "", key="input")
    return input_text


# Creating two lists to store generated and past texts
if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []

# Texting phase
user_input = get_text()

if user_input:
    print(user_input)
    output = generate_response(user_input)
    print(output)
    st.session_state['past'].append(user_input)
    st.session_state['generated'].append(output)

if 'generated' in st.session_state and 'past' in st.session_state:
    for i in range(len(st.session_state['generated']) - 1, -1, -1):
        message(st.session_state['generated'][i], key='generated_' + str(i))
        message(st.session_state['past'][i], key='past_' + str(i), is_user=True)
