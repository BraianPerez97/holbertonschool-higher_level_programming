#!/usr/bin/python3
def list_divisioni(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        try:
            result = my_list_1[1] / my_list_2[i]
        except ZeroDivisionError:
            print ("division by 0")
            result = 0
        except TypeError:
            print("wrong type")
        except IndexError:
            new_list.append(result)

    return (new_list)
