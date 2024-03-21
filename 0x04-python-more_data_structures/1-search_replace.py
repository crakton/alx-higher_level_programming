#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    for x in new_list:
        i = new_list.index(x)
        new_list[i] = replace if x == search else x
    return new_list
