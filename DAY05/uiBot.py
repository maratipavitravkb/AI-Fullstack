import ollama
import streamlit as st
st.title(":red[Welcome] :blue[ to AI Chatbot]")
with st.sidebar:
    personalities = { 
        "kid" : "Give the answers like you are explaining to a 5 years old kid . give answer in 4 lines only",
        "Professor": "You are an IIT  profssor explain the topic using correct technology.Give the answer only  in 4 lines" 
    }
    personality = st.selectbox("Select a personality", personalities.keys())
    if st.button("clear chat"):
        st.session_state.messages =[]
        st.success("Chat cleared successfully!")
    st.header(":blue[chat settings]")
    uploaded_file = st.file_uploader("upload a file...")
    if uploaded_file:
        st.success("file uploaded successfully...")
        if st.button("Display"):
            context = uploaded_file.read().decode("utf-8")
            st.text(context)
if "messages" not in st.session_state:
    st.session_state.messages=[]
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])
question =st.chat_input("you:")
if question:
    with st.chat_message("user"):
        st.write("user: ",question)

st.session_state.messages.append(
    {"role":"user",
    "content":question}
)
with st.spinner("thinking...."):
    response =ollama.chat(
            model="llama3.2:3b",
            messages=[{ 
                "role": "system" , "content" : personalities[personality]
             }]  + st.session_state.messages
        )
st.session_state.messages.append(
        {"role":"assistant",
         "content":response["message"]["content"]
        }
    )
with st.chat_message("assistant"):
    st.write("AI:",response["message"]["content"])