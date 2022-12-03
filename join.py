import streamlit as st
import pandas as pd
from database import get_guardian
    
def join():
    selected_operation = st.selectbox("Choose operation", ["show guardian"])
    if selected_operation == "show guardian":
        srn = st.text_input("Enter SRN")
        cols = ["dependent_id","name","relation","phone","address","dob","age"]
        if st.button("Get info"):
            data = get_guardian(srn)
            st.write("The following are the dependents of srn {}".format(srn))
            df = pd.DataFrame(data,columns=cols)
            st.dataframe(df)
        
        