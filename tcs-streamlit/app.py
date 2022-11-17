from database import Database
import streamlit as st
from my_component import st_custom_slider

# Initialization 
db = Database()



st.title("Students Records")

# Store and display the return value of your custom component
id = st_custom_slider("student_id",0,10,"ans")[0]


st.write(id)

rows = db.filter_by_grade(id['grade'])

# Data Visualization 
for row in rows:
    # st.write(f"{row[0]} has a :{row[1]}:")
    st.write(row)

all_data = db.get_all()
# Data Visualization 
for row in all_data:
    # st.write(f"{row[0]} has a :{row[1]}:")
    st.write(row)


