import streamlit as st
import pandas as pd
from database import get_capacity_info

def aggregate():
    selected_operation = st.selectbox("Choose operation", ["show capacity info"])
    if selected_operation == "show capacity info":
        data = get_capacity_info()
        cols = ["unit_no","count","capacity","available"]
        df = pd.DataFrame(data,columns=cols)
        st.dataframe(df)