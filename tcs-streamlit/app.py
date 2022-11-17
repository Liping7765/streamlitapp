from database.database import Database
import streamlit as st
import pandas as pd
from react_components import st_custom_selector

# Initialization 
db = Database()

st.title("Students Records")

#Store and display the return value of your custom component
results = st_custom_selector()

rows = []
selected_grade = results["grade"]

if not selected_grade: 
   rows = db.get_all()
else:
   rows = db.filter_by_grade(selected_grade)

df = pd.DataFrame(
   rows,
   columns=['ID',"First Name", "Last Name", "Grade", "Lat", "Long"],
   )

st.table(df[['ID',"First Name", "Last Name", "Grade"]])
