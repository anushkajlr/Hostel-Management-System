import streamlit as st
import pandas as pd
from database import retrieve_tables
from database import selected_columns
from database import add_data
from database import show
def create():
    list_of_tables = [i[0] for i in retrieve_tables() if i[0]!="attendance"]
    selected_table = st.selectbox("Table to add entries", list_of_tables)
    cols = selected_columns(selected_table)
    result = show(selected_table)
    st.write("View existing data")
    df = pd.DataFrame(result,columns=cols)
    with st.expander("Show Current Table"):
        st.dataframe(df)
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
    if st.button("Add Item"):
        try:

            add_data(inp,selected_table)
            st.success("Item has been successfully added")
            result = show(selected_table)
            df = pd.DataFrame(result,columns=cols)
            with st.expander("Show Updated Table"):
                st.dataframe(df)
        except:
            if selected_table == "student_guardian":
                st.warning("Cant insert more than 2 guardians and try to follow all constraints")
            elif selected_table == "lg":
                st.warning("Enter correct date range and follow all constraints")
            else:
                st.warning("Please enter values that follow all constraints")

    
   