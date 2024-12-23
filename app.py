import streamlit as st
from agent import graph
from utils.chatbot import stream_graph_updates

st.title("ChatGPT-like clone")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        response = st.write_stream(stream_graph_updates(graph=graph, user_input=prompt))
        
    st.session_state.messages.append({"role": "assistant", "content": response})