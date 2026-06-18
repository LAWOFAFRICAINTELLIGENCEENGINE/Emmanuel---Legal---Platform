#



import streamlit as st
from groq import Groq

# 1. Secure Page Configuration
st.set_page_config(page_title="Emmanuel Legal Platform", page_icon="⚖️")

# 2. Master Header & Marketing Hook
st.title("⚖️ Emmanuel Pan-African Legal Platform")
st.markdown("### Official Proprietary Intelligence Engine")
st.success("⚡ **Stop spending 10 hours researching OHADA law. Get a comprehensive, highly accurate legal brief in 10 seconds.**")
st.divider()

# 3. System State Initialization (The Brain & The Vault)
if "payment_verified" not in st.session_state:
    st.session_state.payment_verified = False
if "free_queries_used" not in st.session_state:
    st.session_state.free_queries_used = 0
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

MASTER_ACCESS_KEY = "EMMANUEL-PREMIUM"

# Security check for server keys
try:
    groq_api_key = st.secrets["GROQ_API_KEY"]
    client = Groq(api_key=groq_api_key)
except Exception:
    st.error("System Status: Security Vault Keys Missing. Please check settings.")
    st.stop()

# 4. Display the Chat History (Memory)
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 5. THE FREEMIUM LOGIC & PAYWALL
# If they haven't paid AND they used their 1 free query, show the Paywall.
if not st.session_state.payment_verified and st.session_state.free_queries_used >= 1:
    st.error("🛑 **Free Trial Exhausted. Premium Access Required to Continue.**")
    
    st.markdown("### 1. Select Your Jurisdiction")
    region = st.radio("Where are you currently practicing law?", ["Select Region...", "Within Africa", "International (Outside Africa)"])
    
    if region != "Select Region...":
        if region == "Within Africa":
            monthly_rate = 100
        else:
            monthly_rate = 200
            
        yearly_total = monthly_rate * 12
        
        st.info(f"**Calculated Annual Subscription:**\n* Monthly Rate: **${monthly_rate} USD**\n* **Total Due Today: ${yearly_total} USD** (Billed Annually)")
        
        st.markdown(f"""
        ### 2. Make Your Payment
        * Transfer **${yearly_total}** to the official corporate account.
        * Send your payment receipt to CEO Emmanuel via WhatsApp.
        * Receive your Premium Access Key to unlock unlimited deep-context analysis for 12 months.
        """)
        
        st.divider()
        st.markdown("### 3. Unlock the Intelligence Engine")
        customer_name = st.text_input("Enter Your Full Name:")
        access_key_input = st.text_input("Enter Your Premium Access Key:", type="password")
        
        if st.button("Verify Payment & Unlock Terminal 🔓"):
            if customer_name == "":
                st.error("Please enter your name.")
            elif access_key_input == MASTER_ACCESS_KEY:
                st.session_state.payment_verified = True
                st.success(f"Payment Verified! Welcome, {customer_name}.")
                st.rerun() 
            else:
                st.error("Invalid Access Key. Please ensure your payment is processed.")
                
    st.stop() # Stops them from seeing the chat box

# 6. THE INTELLIGENCE ENGINE (Only visible if Free Query = 0 OR Payment = Verified)
if st.session_state.free_queries_used == 0 and not st.session_state.payment_verified:
    st.info("🎁 **Your First Deep-Dive Analysis is FREE. Ask your question below:**")

user_query = st.chat_input("Enter your legal or historical query here...")

if user_query:
    with st.chat_message("user"):
        st.markdown(user_query)
    
    st.session_state.chat_history.append({"role": "user", "content": user_query})

    with st.chat_message("assistant"):
        with st.spinner("Processing deep-context analysis..."):
            try:
                messages_for_ai = [{"role": "system", "content": "You are a Pan-African expert in corporate law. Tell the full, complete story. Use chapters and bullet points."}]
                messages_for_ai.extend(st.session_state.chat_history)

                chat_completion = client.chat.completions.create(
                    messages=messages_for_ai,
                    model="llama-3.3-70b-versatile",
                    max_tokens=6000, 
                )
                
                ai_response = chat_completion.choices[0].message.content
                st.markdown(ai_response)
                
                st.session_state.chat_history.append({"role": "assistant", "content": ai_response})
                
                # After the AI answers, increase the free count by 1.
                if not st.session_state.payment_verified:
                    st.session_state.free_queries_used += 1
                    st.rerun() # Refresh to instantly trigger the paywall
                
            except Exception as e:
                st.error(f"An error occurred: {e}")


---

### 
