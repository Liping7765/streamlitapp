from database import Database
import streamlit as st
import numpy as np

# Initialization 
db = Database()



st.title("Students Records")

# Store and display the return value of your custom component
# id = st_custom_slider("student_id",0,10,"ans")[0]


# st.write(id)

# rows = db.get_all()

# # Data Visualization 
# for row in rows:
#     # st.write(f"{row[0]} has a :{row[1]}:")
#     st.write(row)



import pandas as pd
import numpy as np

rows = db.get_all()
location_info = [[float(row[4]),float(row[5])] for row in rows]


df = pd.DataFrame(
   rows,
   columns=['ID',"First Name", "Last Name", "Grade", "col", "cols"])

st.table(df)



df = pd.DataFrame(
    location_info,
    columns=['lat', 'lon'])

st.map(df, zoom = 12)