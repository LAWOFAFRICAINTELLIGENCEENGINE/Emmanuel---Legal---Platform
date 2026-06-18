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

# Intelligence Interface
st.subheader("Legal Analysis Terminal")
user_query = st.text_area("Enter your legal query concerning corporate laws across any of the 54 African nations:")

if st.button("Execute Legal Analysis"):
    if user_query:
        # The AI Connection Sequence
        with st.spinner("Processing query through Groq Neural Network..."):
            try:
                chat_completion = client.chat.completions.create(
                    messages=[
                        {
                            "role": "system",
                            "content": "You are a highly intelligent corporate lawyer specializing in Pan-African jurisdictions, OHADA laws, and the AfCFTA. Provide accurate, professional, and clear legal analysis. Do not hallucinate laws."
                        },
                        {
                            "role": "user",
                            "content": user_query
                        }
                    ],
                    model="llama-3.3-70b-versatile",
                )
                
                # Display the official answer
                st.success("Analysis Complete:")
                st.write(chat_completion.choices[0].message.content)
                
            except Exception as e:
                st.error(f"An error occurred during communication with the AI: {e}")
    else:
        st.warning("Please enter a legal query to begin analysis.")




### 
