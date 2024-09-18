import pandas as pd
import plotly as px
import streamlit as st
st.header('file upload app 2')
file =st.file_uploader('upload dataset',type=['csv'])
if file is not None:
  df=pd.read_csv(file)
  st.write(df)
num_row=st.slider('choose num rows',min_value=1,max_value=len(df))
names_column=st.multiselect('choose columns',df.columns.to_list())
st.write(df[:num_row][names_column])
if names_column:
  st.write(df[:num_row][names_column])
else:
  st.write(df[:num_row])
num_col=df.select_dtypes(include='number').column.to_list()
x_col=st.selectbox('choose x axis',num_col)
y_col=st.selectbox('choose y axis',num_col)
color=st.selectbox('choose color',df.columns.to_list())
fig=px.scatter(x=x_col,y=y_col,color=color)
st.pyplot_chart(fig)

