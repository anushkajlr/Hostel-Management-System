import pandas as pd
import streamlit as st
from database import selected_columns
from database import retrieve_tables
from database import show
from database import delete_data

def delete():
    list_of_tables = [i[0] for i in retrieve_tables()]
    selected_table = st.selectbox("Table to delete entries", list_of_tables)
    cols = selected_columns(selected_table)
    result = show(selected_table)
    df = pd.DataFrame(result,columns=cols)
    with st.expander("Current Data"):
        st.dataframe(df)
    x = len(result)
    selected_option = st.selectbox("Choose method of deletion",['Delete by Sno','Delete by condition'])
    if selected_option == "Delete by Sno":
        record_delete = st.number_input("Select record number to delete")
        if record_delete<0 or record_delete>=x:
            st.warning("wrong type of record selected")
        else:
            st.warning("Are you sure you want to delete {}".format(result[int(record_delete)]))
            if st.button("Delete Record"):
                delete_data(selected_table,result[int(record_delete)])
                st.success("Your record has been deleted!")
                result = show(selected_table)
                df = pd.DataFrame(result,columns=cols)
                with st.expander("Show Updated Table"):
                    st.dataframe(df)
    elif selected_option == 'Delete by condition':
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
        st.warning("Are you sure you want to delete data of form {}".format(inp))
        if st.button("Delete Record"):
            delete_data(selected_table,inp)
            st.success("Your record has been deleted!")
            result = show(selected_table)
            df = pd.DataFrame(result,columns=cols)
            with st.expander("Show Updated Table"):
                st.dataframe(df)
        

            
