import streamlit as st
import os
import datetime

if not os.path.exists('chat_history.txt'):
    with open('chat_history.txt', 'w') as file:
        file.write("Welcome to the chat!\n")

def page():

    st.header("Chat")

    with st.form(key='chat_form'):
        username = st.text_input("Username")
        message = st.text_input("Message")
        submit_button = st.form_submit_button(label='Send')

    if submit_button:
        with open('chat_history.txt', 'a') as file:
            file.write(f"{datetime.datetime.now().strftime('%m/%d %H:%M')}----{username}: {message}  \n")

    # Display the chat history
    with open('chat_history.txt', 'r') as file:
        chat_history = file.read()
    with st.container(border=True):
        st.write(chat_history)


    if st.button("Go back"):
        st.session_state["page"] = "landing"
        st.rerun()