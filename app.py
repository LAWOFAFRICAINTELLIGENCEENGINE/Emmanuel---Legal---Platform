##




import streamlit as st
from groq import Groq

# 1. Secure Page Configuration
st.set_page_config(page_title="Emmanuel Legal Platform", page_icon="⚖️")

# 2. Master Header
st.title("⚖️ Emmanuel Pan-African Legal Platform")
st.markdown("### Official Proprietary Intelligence Engine")
st.divider()

# --- THE DYNAMIC PRICING & MONETIZATION GATEWAY ---
if "payment_verified" not in st.session_state:
    st.session_state.payment_verified = False

# Your master password that you give to lawyers AFTER they pay the yearly fee
MASTER_ACCESS_KEY = "EMMANUEL-PREMIUM"

if not st.session_state.payment_verified:
    st.subheader("🔒 Premium Access Required")
    st.warning("This advanced intelligence engine requires an annual premium subscription to operate.")
    
    st.markdown("### 1. Select Your Jurisdiction")
    st.write("Pricing is calculated based on your geographic region of practice.")
    
    # The intelligent pricing calculator
    region = st.radio("Where are you currently practicing law?", ["Select Region...", "Within Africa", "International (Outside Africa)"])
    
    if region != "Select Region...":
        # Calculate the exact monthly and yearly amounts
        if region == "Within Africa":
            monthly_rate = 100
        else:
            monthly_rate = 200
            
        yearly_total = monthly_rate * 12
        
        # Display the official invoice on screen
        st.info(f"**Calculated Annual Subscription:**\n* Monthly Rate: **${monthly_rate} USD**\n* **Total Due Today: ${yearly_total} USD** (Billed Annually)")
        
        # Payment Instructions
        st.markdown(f"""
        ### 2. Make Your Payment
        To unlock the platform for 12 months, you must pay the full yearly amount of **${yearly_total} USD**.
        
        * **Step 1:** Transfer **${yearly_total}** via Wire Transfer or Bank Deposit. Contact the CEO directly for the official corporate account details.
        * **Step 2:** Send your payment receipt via WhatsApp or Email.
        * **Step 3:** Upon verification, you will receive your **Premium Access Key**.
        """)
        
        st.divider()
        
        # The Final Security Lock
        st.markdown("### 3. Unlock the Intelligence Engine")
        customer_name = st.text_input("Enter Your Full Name:")
        access_key_input = st.text_input("Enter Your Premium Access Key:", type="password")
        
        submit_payment = st.button("Verify Payment & Unlock Terminal 🔓")
        
        if submit_payment:
            if customer_name == "":
                st.error("Please enter your name to proceed.")
            elif access_key_input == MASTER_ACCESS_KEY:
                st.session_state.payment_verified = True
                st.success(f"Payment Verified! Welcome, {customer_name}. Unlocking system...")
                st.rerun() # Refreshes the app to show the AI
            else:
                st.error(f"Invalid Access Key. Please ensure your payment of ${yearly_total} USD has been processed and you typed the key correctly.")
                
    # Stops the code completely so unpaid users cannot access the AI
    st.stop()


# -----------------------------------------------------------------
# THE SYSTEM UNLOCKS BELOW ONLY AFTER SUCCESSFUL PAYMENT
# -----------------------------------------------------------------

# 3. Security & Master Key Verification
try:
    groq_api_key = st.secrets["GROQ_API_KEY"]
    if st.secrets["ADMIN_USERNAME"] and st.secrets["ADMIN_PASSWORD"]:
        pass 
except Exception:
    st.error("System Status: Security Vault Keys Missing. Please check settings.")
    st.stop()

# 4. Initializing the Neural Network
client = Groq(api_key=groq_api_key)

st.success("System Status: Paid Premium Session Active 🟢")

# The Memory Bank
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# The Sleek Chat Box
user_query = st.chat_input("Enter your premium legal or historical query here...")

if user_query:
    with st.chat_message("user"):
        st.markdown(user_query)
    
    st.session_state.chat_history.append({"role": "user", "content": user_query})

    with st.chat_message("assistant"):
        with st.spinner("Processing deep-context analysis..."):
            try:
                messages_for_ai = [
                    {
                        "role": "system",
                        "content": "You are a highly intelligent Pan-African expert in corporate law and history. Tell the full, complete story. Use chapters, headings, and bullet points. Write as much detail as possible."
                    }
                ]
                messages_for_ai.extend(st.session_state.chat_history)

                chat_completion = client.chat.completions.create(
                    messages=messages_for_ai,
                    model="llama-3.3-70b-versatile",
                    max_tokens=6000, 
                )
                
                ai_response = chat_completion.choices[0].message.content
                st.markdown(ai_response)
                
                st.session_state.chat_history.append({"role": "assistant", "content": ai_response})
                
            except Exception as e:
                st.error(f"An error occurred: {e}")




### 
