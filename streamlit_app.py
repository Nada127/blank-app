st.header("calculate Area")
choose=st.selectbox('choose the shape',['circle','rectangle'])
if choose=='circle':
  r=st.number_input('enter the radius',min_value=1,max_value=100)
  Area=r*r*3.14
elif choose=='rectangle':
  w=st.number_input('enter the width',min_value=1,max_value=100)
  h=st.number_input('enter the hight',min_value=1,max_value=100)
  area=h*w
btn=st.button('calculate')
if btn:
  st.write(f'the area is {area}')
