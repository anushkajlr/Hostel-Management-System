import datetime

import pandas as pd
import streamlit as st
from database import selected_columns
from database import retrieve_tables
from database import show
from database import update_tables
def update():
    list_of_tables = [i[0] for i in retrieve_tables() if i[0]!="attendance"]
    selected_table = st.selectbox("Table to edit entries", list_of_tables)
    cols = selected_columns(selected_table)
    result = show(selected_table)
    df = pd.DataFrame(result,columns=cols)
    with st.expander("Current Data"):
        st.dataframe(df)
    l = [i for i in result]
    selected_row = st.selectbox("select row to update",l)
    inp = []
    col1, col2 = st.columns(2)
    x = int(len(cols)/2)
    if x < len(cols)-x:
        x = len(cols)-x
    with col1:

        for i in range(0,x):
            inp.append(st.text_input(str(cols[i])))
    with col2:

        for i in range(x,len(cols)):
            inp.append(st.text_input(str(cols[i])))
    if st.button("Update Record"):

        s = update_tables(selected_table,selected_row,inp)
        if s == "Worked":
            st.success("Your record has been updated!")
            result = show(selected_table)
            df = pd.DataFrame(result,columns=cols)
            with st.expander("Show Updated Table"):
                st.dataframe(df)
            
        else:
            st.warning("Please enter values according to constraints")

        
    