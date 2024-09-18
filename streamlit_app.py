import time
import streamlit as st
area=None
st.header("Claculate Area")
with st.sidebar:
    shape=st.selectbox("choose the shap",["circle","rectangle"])
if shape=='circle':
    r=st.number_input("enter your radius",min_value=1,max_value=100)
    area=r*r*3.14

elif shape=='rectangle':
    w=st.number_input("enter your width",min_value=1,max_value=100)
    h=st.number_input("enter your height",min_value=1,max_value=100)
    area=w*h             

btn=st.button('calculate')
if btn:
    with st.spinner('loading....'):
        time.sleep(2)
    
    st.write(f"the Area= {area}")
    st.sidebar.title('sidebar')
