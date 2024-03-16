import streamlit as st 
from deep_translator import GoogleTranslator
import streamlit_shadcn_ui as ui

primaryColor = st.get_option("theme.primaryColor")
s = f"""
<style>
div.stButton > button:first-child {{ border: 5px solid {primaryColor}; border-radius:20px 20px 20px 20px; }}
<style>
"""
st.markdown(s, unsafe_allow_html=True)

st.title('English - Marathi Translator')
msgs = st.text_area('Enter text to translate in marathi unicode')


if st.button('Translate'):
    hindi_paragraph = GoogleTranslator(source='en', target='mr').translate(msgs)
    st.markdown('<font color="blue">Your translated text is : </font>', unsafe_allow_html=True)
    st.write(hindi_paragraph)

st.toast('Welcome to my first translator app - :blue[Omi S] :sunglasses:')
