import re 
import streamlit as st


# page styling

st.set_page_config(page_title="Password Strength By Check Nisar Ahmed",page_icon="🔑",layout="centered")

# custom css 
st.markdown("""
    <style>
            .main {text-align:center;}
            .stTextInput {width: 60% !important; margin:auto;}
            .stButton button {width: 50%; background-color #4CAF50; color:white;font-size:18px;}
            .stButton button:hover {background-color:#45a049;}
    </style>          
""",unsafe_allow_html=True)

# page title and description

st.title("🔐 Password Strength Genertor")
st.write("Enter Your Password Below To Check Its Security Level. 🔍")

# check password strength function
def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1 #increased score by 1
    else:
        feedback.append("❌ Password Should Be ** Atleast 8 Character Long **")

    if re.search(r"[A-Z]",password) and re.search("r[a-z]",password):
        score += 1 
    else:
        feedback.append("❌ Password Should Include ** Both Upercase (A-Z) and Lowercase (a-z) Letters **")

    if re.search(r"\d",password):
        score += 1
    else:
        feedback.append("❌ Password Should Include ** Atleast One Number (0-9) **")

    if re.search(r"[!@#$%]",password):
        score += 1
    else:
        feedback.append("❌ Include ** Atleast One Special Character (!@#$%) **.")

    

    # display password strength result
    
    if score == 4:
        st.success("✅  ***Strong Password*** - Your Password Is Score.")
    elif score == 3 :
        st.info("⚠️ ***Moderate  Password*** - Consider Improving Security By Adding More Feature ")
    else:
        st.error("❌ ***Week Password*** - Follow The Suggestion Below To Strength it. ")


# feedback

    if feedback:
     with st.expander(" ***Improve Your Password*** "):
         for item in feedback:
             st.write(item)
password = st.text_input("Enter Your Password:" , type="password", help="Ensure Your Password Is Strong 🔐")


# button working 

if st.button("Check Strength"):
    if password:
        check_password_strength(password)
    else:
        st.warning("Please Enter a Password First! ")
