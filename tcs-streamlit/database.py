import mysql.connector
import streamlit as st


class Database:
    def __init__(self):
        self.conn = mysql.connector.connect(**st.secrets["mysql"])

    def run_query(self, query):
        with self.conn.cursor() as cur:
            cur.execute(query)
            return cur.fetchall()

    # get all records from table for demo 
    def get_all(self):
        sql = "SELECT * from students;"
        return self.run_query(sql)

    # get records by id 
    def get_by_id(self, id = 0):
        @st.experimental_memo(ttl=600)
        def inner(id = 0):
            sql = f"SELECT * from students where student_id = {id};"
            return self.run_query(sql)
        return inner(id)

    # get records by id 
    def filter_by_id(self, id = 0):
        def inner(id = 0):
            sql = f"SELECT * from students where student_id >= {id};"
            return self.run_query(sql)
        return inner(id)

    # get records by grade
    def filter_by_grade(self, grade = 1):
        def inner(grade = 1):
            sql = f"SELECT * from students where grade = {grade};"
            return self.run_query(sql)
        return inner(grade)



    # Perform query.
    # Uses st.experimental_memo to only rerun when the query changes or after 10 min.  
    def add_record(self, firstname, lastname, grade, lat, longi):
        
        @st.experimental_memo(ttl=600)
        def add(firstname, lastname, grade, lat, longi):
            sql = ('INSERT INTO students(firstname, lastname, grade, latitude, longtitude)'
                        f' VALUES ( "{firstname}", "{lastname}", {grade}, {lat}, {longi} )')
            self.run_query(sql)
            self.conn.commit()

        return add(firstname, lastname, grade, lat, longi)
        
    def update_record_with_id(self, id, values):

        #validation check to ensure id exists 
        rows = self.get_by_id(id)
        if not len(rows):
            st.write("data doesnot exist")
            return 

        @st.experimental_memo(ttl=600)
        def update(id, values):
            
            firstname, lastname, grade = values

            sql = f"""
                    UPDATE STUDENTS 
                    SET FIRSTNAME = "{firstname}",
                        LASTNAME = "{lastname}",
                        GRADE = "{grade}"
                    WHERE student_id = {id}
                """
            self.run_query(sql)
            self.conn.commit()

        return update(id, values)

    def delete_with_id(self, id):

        @st.experimental_memo(ttl=600)
        def delete(id):
            sql = f'Delete from students WHERE student_id = {id}'
            self.run_query(sql)
            self.conn.commit()

        return delete(id)
   



    def delete_all(self):

        @st.experimental_memo(ttl=600)
        def delete():
            sql = f'Delete from students'
            self.run_query(sql)
            self.conn.commit()

        return delete()

