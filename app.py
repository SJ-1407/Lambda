import streamlit as st
import os
from utils import get_answer, text_to_speech, autoplay_audio, speech_to_text
from audio_recorder_streamlit import audio_recorder
from streamlit_float import *
from streamlit_mic_recorder import mic_recorder


float_init()

def initialize_session_state():
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "assistant", "content": "Hi! How may I assist you today?"}
        ]


initialize_session_state()

st.title(":green[Lambda] 🤖")

footer_container = st.container()

with footer_container:
 cols = st.columns([0.8,3],gap="small")  


with cols[0]:  
    audio_bytes = mic_recorder(
        start_prompt="Start recording",
        stop_prompt="Stop recording",
        just_once=True,
        use_container_width=False,
        callback=None,
        args=(),
        kwargs={},
        key=None
    )
    if(audio_bytes):
      audio_bytes=audio_bytes['bytes']

with cols[1]: 
   
    if("input" in st.session_state):
        st.text_input("Enter your text query",key="input")
        user_text_input = st.session_state.input
    else:
         user_text_input=st.text_input("Enter your text query",key="input")
    
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

   
if audio_bytes:
    # Write the audio bytes to a file
    with st.spinner("Transcribing..."):
        webm_file_path = "temp_audio.mp3"
        with open(webm_file_path, "wb") as f:
            f.write(audio_bytes)

        transcript = speech_to_text(webm_file_path)
        if transcript:
            st.session_state.messages.append({"role": "user", "content": transcript})
            with st.chat_message("user"):
                st.write(transcript)
            os.remove(webm_file_path)

elif (user_text_input):


    st.session_state.messages.append({"role": "user", "content": user_text_input})
    with st.chat_message("user"):
        st.write(user_text_input)
    
if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Thinking🤔..."):
            final_response = get_answer(st.session_state.messages)
        with st.spinner("Generating audio response..."):    
            audio_file = text_to_speech(final_response)
            autoplay_audio(audio_file)
        st.write(final_response)
        st.session_state.messages.append({"role": "assistant", "content": final_response})
        os.remove(audio_file)

# Float the footer container and provide CSS to target it with
footer_container.float("bottom: 0rem;")