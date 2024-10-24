import streamlit as st
import helper_function
st.title("Restaurant Name generator")
cuisine = st.sidebar.selectbox("Pick a Cuisine", ("Indian", "Italian", "Mexican", "Arabic", "American"))

if cuisine:
    response = helper_function.generate_name(cuisine)
    st.header(response['restaurant_name'].strip())
    menu_items = response['menu_items'].strip().split(",")
    st.write("**Menu Items**")
    for i in menu_items:
        st.write("-", i)