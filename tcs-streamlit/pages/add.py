import streamlit as st
from database.database import Database
import random

with st.form("my_form"):
    col1, col2 = st.columns(2)

    with col1:
        firstname = st.text_input("First Name")
    with col2:
        lastname = st.text_input("Last Name")

    grade = st.selectbox("Grade", (1,2,3,4,5))

    clicked = st.form_submit_button("Add Student")

    data = [firstname, lastname, grade]



    if clicked and "" in data:
        st.error("please ensure to enter all fields.")
    elif clicked:
        db = Database()
        #for demo, location info is generated 
        #newyork_lat = random.random() * random.randint(-1, 1) / 50 + 40.668435
        #newyork_long = random.random() * random.randint(-1, 1) / 50 + -73.948389
        db.add_record(firstname, lastname, grade)
        st.success(f"Student {firstname} {lastname} is added to the database.")

       
        # st.experimental_rerun()

