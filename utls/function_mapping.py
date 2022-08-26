import operations.actions as op
from operations.search_data import SearchUser as src
roles={
    0:["View_User_List", "Show_Details"],
    1:["View_User_List", "Show_Details", "Edit_Details", "Add_User", "Delete_User", "Search_User"]
}

role_fn_mapping={
    "View_User_List":op.show_list,
    "Edit_Details":op.edit_user,
    "Add_User":op.add_user,
    "Delete_User":op.delete_user,
    "Show_Details":op.show_details,
    "Search_User": src
}

