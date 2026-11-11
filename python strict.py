import streamlit as st
from groq import Groq

# 1. पेज की सेटिंग्स (टाइटल और आइकॉन)
st.set_page_config(page_title="Strict Python Tutor", page_icon="🐍")
st.title("🐍 Strict Python Tutor")
st.write("Welcome! Ask me anything about Python. (Warning: I am very strict!)")

# 2. API Key और Client (यहाँ अपनी असली Key डालें)
api_key = "Add your Groq API Key here"
client = Groq(api_key=api_key)

# 3. Memory (History) को सेव रखने के लिए Session State
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are a python tutor. You only answer questions related to python. If the user asks anything unrelated, scold them and tell them to focus on python."}
    ]

# 4. पुरानी चैट को स्क्रीन पर दिखाना
for message in st.session_state.messages:
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.write(message["content"])

# 5. यूज़र से नया मैसेज लेना
if user_input := st.chat_input("Type your Python question here..."):
    
    # यूज़र का मैसेज स्क्रीन पर दिखाना और सेव करना
    with st.chat_message("user"):
        st.write(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # AI से जवाब लेना
    with st.spinner("Thinking..."):
        response = client.chat.completions.create(
            messages=st.session_state.messages,
            model="openai/gpt-oss-120b"
        )
        ai_reply = response.choices[0].message.content
        
    # AI का जवाब स्क्रीन पर दिखाना और सेव करना
    with st.chat_message("assistant"):
        st.write(ai_reply)
    st.session_state.messages.append({"role": "assistant", "content": ai_reply})
