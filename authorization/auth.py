import getpass
import hashlib
from utils.db_connection import DbConnection
import utils.xml_parse as xml_object
from user.user import User

class Auth:
    def __init__(self):
        self.id=int(input("Enter user id : "))
        self.verify()

    def verify(self):
        obj=DbConnection()
        db_cursor=obj.get_instance().cursor()
        db_cursor.execute((xml_object.root[2][0].text).format(self.id))
        login_record=db_cursor.fetchall()

        if len(login_record)==0:
            print("User not found!")
        else:
            self.password=getpass.getpass("Enter password : ")
            if hashlib.sha256(self.password.encode('utf-8')).hexdigest()==login_record[0][1]:
                print("Login successful")
                self.create_user_obj(login_record[0][2])
            else:
                print("Access denied!")

    def create_user_obj(self, role_id):
        User(self.id,role_id)


