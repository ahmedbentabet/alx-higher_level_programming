#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    try:
        for i in range(list_length):
            try:
                if not isinstance(my_list_1[i], (int, float)) or not isinstance(my_list_2[i], (int, float)):
                    print('wrong type')
                    new_list.append(0)
                elif my_list_2[i] == 0:
                    raise ZeroDivisionError
                else:
                    new_list.append(my_list_1[i] / my_list_2[i])
            except IndexError:
                print('out of range')
                new_list.append(0)
            except ZeroDivisionError:
                print('division by 0')
                new_list.append(0)
    finally:
        return new_list
