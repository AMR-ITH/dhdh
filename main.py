import streamlit as st

st.title('Campusx')

col1,col2=st.columns(2)

with col1:
    st.image('Screenshot (439).png')

with col2:
    st.header('CampusX is a ONlinr PlatFoRm')

st.header('Courses')
st.subheader('DSMP')

st.subheader('DSA')


st.sidebar.title('Menu')
st.sidebar.markdown("""
- Home
- About
- Contact
- career
- login
""")


option=st.sidebar.selectbox('select one',['teacher','child'])
btn=st.sidebar.button('Select')

if btn:
    st.title("hello teacher"+option)

