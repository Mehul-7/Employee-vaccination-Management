import utils.xml_parse as xml_object
from utils.db_connection import DbConnection
from prettytable import PrettyTable
from rich import print
db_conn=DbConnection.get_instance()

class SearchUser:
    def __init__(self):
        self.param=input("Enter search parameter : ")
        self.search()
    
    def search(self):
        db_cursor=db_conn.cursor()
        db_cursor.execute((xml_object.root[2][6].text).format(self.param))
        search_result=db_cursor.fetchall()
        if len(search_result)==0:
            print(xml_object.root[3][0].text)
        else:
            my_table = PrettyTable(["iD", "user_name", "Date of Birth", "Contact" , "Gender"]) 
            for details in search_result:
                my_table.add_row([details[0] , details[1],details[2],details[3],details[4]])
            print(my_table)

