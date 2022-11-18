from database.database import Database
import streamlit as st
import pandas as pd
from react_components import st_custom_selector


#
@st.cache
def filter_by_grade(rows, grade):

    if grade == 0:
        return [row[:4] for row in rows]

    result = []
    for row in rows :
        if row[3] == grade :
            result.append(row[:4])

    return result 


# Initialization 
db = Database()
st.title("Students Records")

#Store and display the return value of your custom component


results = st_custom_selector()

rows = filter_by_grade(db.get_all(), 0)
selected_grade = results["grade"]



if selected_grade: 
   rows = filter_by_grade(rows, selected_grade)

df = pd.DataFrame(
   rows,
   columns=['ID',"First Name", "Last Name", "Grade"],
)

st.table(df)
