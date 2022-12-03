import streamlit as st
import pandas as pd
from database import execute_query
def enter_query():
    s = st.text_input("Enter query")
    
    if st.button("Execute"):
        try:
            data1,data2 = execute_query(s)
            df = pd.DataFrame(data2,columns=data1)
            st.dataframe(df)
        except:
            st.warning("Your query has an error")