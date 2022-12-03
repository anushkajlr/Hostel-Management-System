import streamlit as st
import pandas as pd
from database import get_bonus_info
from database import selected_columns

def set():
    salary = st.number_input("Enter threshold salary")
    years = st.number_input("Enter threshold years worked")
    if st.button("get info"):
        data = get_bonus_info(salary,years)
        cols = selected_columns("staff")
        cols.append("years_worked")
        st.write("The following staff qualify for a bonus")
        df = pd.DataFrame(data,columns=cols)
        st.dataframe(df)