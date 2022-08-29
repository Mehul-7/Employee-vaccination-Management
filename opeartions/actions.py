from utils.db_connection import DbConnection
import utils.xml_parse as xml_object
import datetime
import hashlib
from prettytable import PrettyTable
from rich import print

db_conn=DbConnection.get_instance()

def show_list():
    user_list=execute_query(xml_object.root[2][5].text).fetchall()
    if len(user_list)==0:
        print(xml_object.root[3][0].text)
    else:
        my_table = PrettyTable(["ID" , "user_name"])
        for x in user_list:
            my_table.add_row([x[0] , x[1]])
        print(my_table)
        print()

def show_details():
    user_id=input(xml_object.root[0][6].text)
    details=execute_query((xml_object.root[2][1].text).format(user_id)).fetchall()
    try:
        details[0][0]
    except IndexError:
        print(xml_object.root[3][0].text)
        return 0
    else:
        my_table = PrettyTable(["iD", "user_name", "Date of Birth", "Contact" , "Gender" , "Dose Id" , "Date of Vaccination" , "Dose Type" , "Vaccine Name"])
        my_table.add_row([details[0][0] , details[0][1],details[0][2],details[0][3],details[0][4],details[0][6],details[0][7],details[0][8],details[0][9]])
        print(my_table)
        return 1


def add_user():
    user_id=input(xml_object.root[0][6].text)
    if ((execute_query((xml_object.root[2][10].text).format(user_id))).fetchone())[0]==1:
        print("[bold red]USER ALREADY EXISTS![/bold red]")
    else:
        user_name=input("Enter user name : ")
        date_entry = input(xml_object.root[0][7].text)
        year, month, day = map(int, date_entry.split('-'))
        dob = datetime.date(year, month, day)
        contact=int(input("Enter contact no. : "))
        gender=input("Enter gender: ")
        password=input("Create password : ")
        execute_query((xml_object.root[2][2].text).format(user_id, user_name, dob, contact, gender, hashlib.sha256(password.encode('utf-8')).hexdigest()))
        execute_query((xml_object.root[2][9].text).format(user_id, 0))
        db_conn.commit()
        print("[bold green]USER ADDED SUCCESSFULLY[/bold green]")
        print()

def delete_user():
    user_id=input(xml_object.root[0][6].text)
    if ((execute_query((xml_object.root[2][10].text).format(user_id))).fetchone())[0]==1:
        db_cursor=db_conn.cursor()
        db_cursor.callproc('remove_user',[user_id,])
        db_cursor.close()
        db_conn.commit()
        print("[bold green]USER REMOVED SUCCESSFULLY[/bold green]")
    else:
        print(xml_object.root[3][0].text)

def edit_user():
    if show_details()==1:
        print("Enter new details")
        user_name=input("Enter user name : ")
        date_entry = input(xml_object.root[0][7].text)
        year, month, day = map(int, date_entry.split('-'))
        dob = datetime.date(year, month, day)
        contact=int(input("Enter contact no. : "))
        gender=input("Enter gender: ")
        _password=input("Create password : ")
        execute_query((xml_object.root[2][4].text).format( user_name, dob, contact, gender, hashlib.sha256(_password.encode('utf-8')).hexdigest()))

        db_conn.commit()
        print("[bold green]Data updated Succesfully[/bold green]")

def add_dosage():
    _id=input("Enter user id : ")
    print("ENTER DOSAGE DETAILS \n")
    user_id = input("Last four digits of Adhaar card : " + xml_object.root[0][6].text)
    date_entry = input(xml_object.root[0][7].text)
    year, month, day = map(int, date_entry.split('-'))
    date = datetime.date(year, month, day)
    dose_type = input("1. First Dose \n2. Second Dose \n3. Third Dose\n")
    print("Enter Vaccination Type : ")
    execute_query((xml_object.root[2][7].text).format(user_id,  date, dose_type))
    db_conn.commit()
    if ((execute_query((xml_object.root[2][11].text).format(_id))).fetchone())[0]==0:
        inp = input("1. Covaxin\n2. Sputnik\n")
        execute_query((xml_object.root[2][8].text).format(user_id, _id, inp))
        db_conn.commit()

    print("[bold green]Dosage info Added[/bold green]")


def execute_query(query):
    db_cursor=db_conn.cursor()
    db_cursor.execute(query)
    return db_cursor
