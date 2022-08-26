import utils.function_mapping as fm

class User:
    def __init__(self , id, role_id):
        self._user_id=id
        self._role=role_id
        self.panel()

# Choose from the list of available actions for the user
    def panel(self):
        choice=-1
        while True:
            index=0
            print("---------USER PANEL---------")
            for x in fm.roles[self._role]:
                print(f"{index} : {x}")
                index += 1
            print("6 : Sign out")
            choice = int(input())
            if choice==6:
                break
            fm.role_fn_mapping[fm.roles[self._role][choice]]()




