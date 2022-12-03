
import streamlit as st
import mysql.connector

from read import read
from create import create
from join import join
from aggregate import aggregate
from set import set
from delete import delete
from update import update
from attendance import attendance
from enter_query import enter_query

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
)
c = mydb.cursor()


def main():
    st.title("Hostel Management System")
    menu = ["Add Entries", "View Tables", "Edit Data", "Remove Data","Show guardian - Join","See capacity - Aggregate","Evaluate bonus - Set","Take Attendance","Enter query"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "View Tables":
        read()
    elif choice == "Add Entries":
        create()
    elif choice == "Show guardian - Join":
        join()
    elif choice =="See capacity - Aggregate":
        aggregate()
    elif choice == "Evaluate bonus - Set":
        set()
    elif choice == "Remove Data":
        delete()
    elif choice == "Edit Data":
        update()
    elif choice == "Take Attendance":
        attendance()
    elif choice == "Enter query":
        enter_query()


   


if __name__ == '__main__':
    main()
