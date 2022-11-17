import streamlit as st
from database import Database
import time


db = Database()
rows = db.get_all()

ids = [ row[0] for row in rows ]

op1, op2, op3 = st.columns([2,1,6])

with op1:
    selected_id = st.selectbox("ID", tuple(ids))
with op2:
    agree = st.checkbox('Edit')

disabled = not agree

student = {}
for row in rows:
    if selected_id == row[0]:
        student = row

with st.form("update_form"):
    col1, col2 = st.columns(2)
    with col1:
        firstname = st.text_input("First Name", disabled = disabled, value = student[1])
    with col2:
        lastname = st.text_input("Last Name", disabled = disabled, value = student[2])

    # grade = st.selectbox("Grade", (1,2,3,4,5))
    grade = st.text_input("Grade", disabled = disabled, value = student[3])

    clicked = st.form_submit_button("Update Student")

    data = [firstname, lastname, grade]

    if clicked and "" in data:
        st.error("please ensure to enter all fields.")
    elif clicked:
        db = Database()
        db.update_record_with_id(selected_id,data)
        st.success(f"Student {firstname} {lastname} is updated to the database.")
        time.sleep(2)
        st.experimental_rerun()