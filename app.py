#


import streamlit as st
from groq import Groq

# Secure Page Configuration
st.set_page_config(page_title="Emmanuel Legal Platform", page_icon="⚖️")

# Master Header
st.title("⚖️ Emmanuel Pan-African Legal Platform")
st.markdown("### Official Proprietary Intelligence Engine")
st.write("Providing secure, deep-context legal analysis across African jurisdictions, including OHADA laws and the African Continental Free Trade Area (AfCFTA).")

st.divider()

# Security & Master Key Verification
try:
    # Pulling the keys from your secure vault
    groq_api_key = st.secrets["GROQ_API_KEY"]
    if st.secrets["ADMIN_USERNAME"] and st.secrets["ADMIN_PASSWORD"]:
        st.success("System Status: Secure Master Connection Established 🟢")
except Exception:
    st.error("System Status: Security Vault Keys Missing. Please check Streamlit Advanced Settings.")
    st.stop()

# Initializing the Neural Network
client = Groq(api_key=groq_api_key)

# --- THE MEMORY BANK ---
# If the app just started, create a blank memory bank
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Display all previous messages from the memory bank on the screen
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- THE CHAT INTERFACE ---
# This creates a professional chat box at the bottom of the screen
user_query = st.chat_input("Enter your legal query concerning corporate laws...")

if user_query:
    # 1. Show the user's question on the screen instantly
    with st.chat_message("user"):
        st.markdown(user_query)
    
    # 2. Save the user's question to the Memory Bank
    st.session_state.chat_history.append({"role": "user", "content": user_query})

    # 3. Contact the Intelligence Engine
    with st.chat_message("assistant"):
        with st.spinner("Processing query through Groq Neural Network..."):
            try:
                # Prepare the brain: Give it the system rules AND the entire chat history
                messages_for_ai = [
                    {
                        "role": "system",
                        "content": "You are a highly intelligent corporate lawyer specializing in Pan-African jurisdictions, OHADA laws, and the AfCFTA. Provide accurate, professional, and clear legal analysis. Do not hallucinate laws."
                    }
                ]
                # Attach the memory bank
                messages_for_ai.extend(st.session_state.chat_history)

                # Send everything to Groq
                chat_completion = client.chat.completions.create(
                    messages=messages_for_ai,
                    model="llama-3.3-70b-versatile",
                )
                
                # Extract the final answer
                ai_response = chat_completion.choices[0].message.content
                
                # Print the answer to the screen
                st.markdown(ai_response)
                
                # Save the answer to the Memory Bank so it remembers for next time
                st.session_state.chat_history.append({"role": "assistant", "content": ai_response})
                
            except Exception as e:
                st.error(f"An error occurred during communication with the AI: {e}")


---

### 
