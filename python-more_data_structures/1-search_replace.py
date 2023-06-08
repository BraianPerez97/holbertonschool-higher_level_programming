#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    for i in range(new_list.count(search)):
        new_list.insert(new_list.index(search), replace)
        new_list.remove(search)
    return (new_list)
