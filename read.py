import pandas as pd
import streamlit as st
import plotly.express as px
from database import show
from database import retrieve_tables
from database import selected_columns

def read():
    list_of_tables = [i[0] for i in retrieve_tables()]
    selected_table = st.selectbox("Table to view", list_of_tables)  
    result = show(selected_table)
    cols = selected_columns(selected_table)
    df = pd.DataFrame(result,columns=cols)
    st.dataframe(df)

  