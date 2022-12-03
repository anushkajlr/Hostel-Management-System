
import mysql.connector
import streamlit as st 
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    database="hostel_project"
)
c = mydb.cursor()

def retrieve_tables():
    c.execute("SHOW TABLES")
    data = c.fetchall()
    return data
def show(table):
    c.execute("SELECT * FROM {}".format(table))
    data = c.fetchall()
    return data
def selected_columns(table):
    c.execute("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '{}' ORDER BY ORDINAL_POSITION".format(table))
    data = c.fetchall()
    data = [i[0] for i in data]
    return data
def add_data(inp,table):
    inp = [int(i) if i.isdigit() == True else i for i in inp]
    inp = tuple(inp)
    c.execute("INSERT INTO {} VALUES{}".format(table,inp));
    mydb.commit()
def get_guardian(srn):
    c.execute("SELECT DISTINCT guardian.dependent_id,name,relation,phone,address,dob,calc_age(dob) from student_guardian JOIN guardian WHERE srn = '{}'".format(srn))
    data = c.fetchall()
    return data
def get_capacity_info():
    c.execute("SELECT student_info.unit_no, count(student_info.srn) as count,capacity,capacity-count(student_info.srn) as available from student_info NATURAL JOIN unit group by unit_no")
    data = c.fetchall()
    return data
def get_bonus_info(salary,years):
    c.execute("SELECT staff_id,unit_no,name,occupation,salary,dob,doj,calc_age(doj) from staff where salary < {} INTERSECT SELECT staff_id,unit_no,name,occupation,salary,dob,doj,calc_age(doj) from staff where (DATEDIFF(curdate(),doj)/365.2425) > {}".format(salary,years))
    data = c.fetchall()
    return data
def view_all_data(table):
    c.execute("SELECT * FROM {}".format(table))
    data = c.fetchall()
    return data
def delete_data(table,values):
    s = "DELETE FROM {} WHERE ".format(table)
    col = selected_columns(table)
    for i in range(len(col)):
        if(values[i]!=""):
            if type(values[i]) == int:
                s += "{} = {} and ".format(col[i],values[i])
            else:
                s += "{} = '{}' and ".format(col[i],values[i])
    s = s[:-5]
    c.execute(s)
    mydb.commit()

def update_tables(table,entry,new_entry):
    s = "UPDATE {} SET ".format(table)
    col = selected_columns(table)
    for i in range(len(col)):
        if(new_entry[i]!=""):
            if type(new_entry[i]) == int or str(new_entry[i]).isdigit() == True:
                s += "{} = {}, ".format(col[i],new_entry[i])
            else:
                s += "{} = '{}', ".format(col[i],new_entry[i])
    s = s[:-2]
    s+= " WHERE "
    for i in range(len(col)):
        if(entry[i]!="" and str(entry[i]) != "None"):
            if type(entry[i]) == int or str(entry[i]).isdigit() == True:
                s += "{} = {} and ".format(col[i],entry[i])
            else:
                s += "{} = '{}' and ".format(col[i],entry[i])
    s = s[:-5]
    try:

        c.execute(s)
        mydb.commit()
        return "Worked"
    except:
        return "Error"
        
def fetch_students():
    c.execute("select srn from student")
    data = c.fetchall()
    return data
def add_data_attendance(srn):
    c.execute("insert into attendance values('{}')".format(srn))
    mydb.commit()
def select_absent():
    c.execute("with t(srn) as (select srn from student_info except select * from attendance) select t.srn from t LEFT JOIN lg ON t.srn = lg.srn where lg.srn IS NULL or DATEDIFF(end_date,curdate()) <0  or DATEDIFF(start_date,curdate())>0")
    data = c.fetchall()
    return data
def start_attendance():
    c.execute("DELETE FROM attendance")
    mydb.commit()

def execute_query(s):
    c.execute(s)
    data1 = c.description
    data1 = [i[0] for i in data1]
    data2 = c.fetchall()
    return [data1,data2]


def show_lg():
    c.execute("SELECT srn from lg where DATEDIFF(curdate(),start_date)>0 and DATEDIFF(end_date,curdate())>0")
    data = c.fetchall()
    return data
