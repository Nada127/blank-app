 
%%writefile app.py
import streamlit as st
name =st.text_input("Enter your name")
btn=st.button("show")
if btn:
  st.write(f'hello{name}')
