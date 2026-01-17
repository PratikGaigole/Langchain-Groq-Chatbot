import streamlit as st
import dotenv 

import langchain 
from langchain_groq import ChatGroq


from dotenv import load_dotenv
load_dotenv()

import os

st.set_page_config(page_title="Chat Bot", page_icon= "🤖")
st.title("Chat Bot With Langchain And Streamlit")

#prompt=st.chat_input("Type Your Query")

if "conv" not in st.session_state:
    st.session_state["conv"] = []
    st.session_state["memory"] = []
    st.session_state["memory"].append(("system", "act like a 25 years old men"))

for y in st.session_state["conv"]:
    with st.chat_message(y["role"]):
        st.write(y["content"])

prompt = st.chat_input("Type Your Query")

if prompt:
    st.session_state["conv"].append({"role":"user", "content":prompt})
    st.session_state["memory"].append(("user", prompt))

    with st.chat_message("user"):
        st.write(prompt)

    model=ChatGroq(
        model="llama-3.1-8b-instant",
        temperature=0.3)


    response = model.invoke(st.session_state["memory"])

    with st.chat_message("ai"):
        st.write(response.content)

    st.session_state["conv"].append({"role":"ai", "content":response.content})
    st.session_state["memory"].append(("ai",response.content))
