#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == []:
        return 0

    dividend = 0
    divided = 0
    for tuple in my_list:
        dividend += tuple[0] * tuple[1]
        divided += tuple[1]

    result = dividend / divided
    return result
