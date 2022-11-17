import streamlit as st
from database.database import Database


db = Database()
rows = db.get_all()

users_info = (row[0] for row in rows )


selected_id = st.selectbox("ID", users_info)

disabled = True

student = {}
for row in rows:
    if selected_id == row[0]:
        student = row

with st.form("delete_form"):
    col1, col2 = st.columns(2)
    with col1:
        firstname = st.text_input("First Name", disabled = disabled, value = student[1])
    with col2:
        lastname = st.text_input("Last Name", disabled = disabled, value = student[2])

    # grade = st.selectbox("Grade", (1,2,3,4,5))
    grade = st.text_input("Grade", disabled = disabled, value = student[3])

    clicked = st.form_submit_button("Delete Student")

    if clicked:
        db = Database()
        db.delete_with_id(selected_id)
        st.success(f"Student {firstname} {lastname} is deleted from the database.")
        st.experimental_rerun()