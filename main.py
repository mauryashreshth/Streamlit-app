import streamlit as st
from streamlit_chat import message
from bardapi import Bard
dilKiBaat = 'XwgvfPVECktBPQ9gS64EuzKMqQ_yv0jgV4vXTRk0Ek0cIzewNhoX0xmpZzBl671RXzt8ug.'
bard = Bard(token=dilKiBaat)

st.set_page_config(page_title="AI BOT")
st.markdown(
    '''
    <html>
        <head>
            <title>AI BOT</title>
        </head>
    </html>
    <style>
        [data-testid="stAppViewContainer"] {
            background-image: url("https://c4.wallpaperflare.com/wallpaper/306/908/890/spots-background-light-dark-wallpaper-preview.jpg");
            background-size: cover;
        }
        .body {
            background-color: transparent !important;
        }
    </style>
    ''',
    unsafe_allow_html=True,
)

st.title("Tutoring Bot")


# Function to generate a response
def genrateRes(prompt):
    response = bard.get_answer(prompt)['content']
    return response


def get_text():
    input_text = st.text_input("Puneet Bot: ", "", key="input")
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
    output = genrateRes(user_input)
    print(output)
    st.session_state['past'].append(user_input)
    st.session_state['generated'].append(output)

if st.session_state['generated']:
    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state['generated'][i], key = 'generated_'+str(i)) # We use message to display the generated message in reverse order. The key is used to store unique item
        message(st.session_state['past'][i], key = 'past_'+str(i), is_user=True) # We use message to display the past message in reverse order. The key is used to mark it as unique


