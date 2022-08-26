import utils.xml_parse as xml_object
from authorization.auth import Auth
from utils.db_connection import DbConnection

def main():
    while True:
        print()
        print("----------------------{}----------------".format("MAIN MENU"))
        print("1. {}".format(xml_object.root[0][0].text) )
        print("2. EXIT")
        print()

        option = int(input("Enter option "))
        match int(option):
            case 1:
                Auth()
            case 2:
                DbConnection.get_instance().close()
                break


if __name__=='__main__':
    main()
