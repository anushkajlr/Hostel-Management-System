import pandas as pd
import streamlit as st
from database import fetch_students
from database import add_data_attendance
from database import show
from database import selected_columns
from database import select_absent
from database import start_attendance
from database import show_lg
def attendance():
    selected_method = st.selectbox("Choose Method",["Through search box","Through typing"])
    if selected_method == "Through search box":
        all_students = [i[0] for i in fetch_students()]
        selected_srn = st.selectbox("Mark Present", all_students)
        if st.button("mark_present"):
            try:
                add_data_attendance(selected_srn)
                st.success("{} marked present".format(selected_srn))

            except:
                st.warning("Student has already been marked present or student doesnt exist")

    elif selected_method == "Through typing":
        selected_srn = st.text_input("Enter the srn")
        if st.button("mark_present"):
            try:
                add_data_attendance(selected_srn)
                st.success("{} marked present".format(selected_srn))
            except:
                st.warning("Student has already been marked present or student doesnt exist")
    cols = selected_columns("attendance")
    result = show("attendance")
    df = pd.DataFrame(result,columns=cols)
    with st.expander("List of students present"):
            st.dataframe(df)
    absent_not_lg = select_absent()
    cols = selected_columns("attendance")
    df = pd.DataFrame(absent_not_lg,columns=cols)
    with st.expander("See absentees"):
        st.dataframe(df)
    data = show_lg()
    df = pd.DataFrame(data,columns=cols)
    with st.expander("See students on lg"):
        st.dataframe(df)
    if st.button("Reset Attendance"):
        start_attendance()
