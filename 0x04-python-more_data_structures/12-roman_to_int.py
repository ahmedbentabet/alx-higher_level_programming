#!/usr/bin/python3
def roman_to_int(roman_string):
    my_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    int = 0

    if isinstance(roman_string, str):
        for i in range(len(roman_string) - 1):
            if my_dict[roman_string[i]] >= my_dict[roman_string[i + 1]]:
                int += my_dict[roman_string[i]]
            elif my_dict[roman_string[i]] < my_dict[roman_string[i + 1]]:
                int -= my_dict[roman_string[i]]
        int += my_dict[roman_string[-1]]
        return int
    elif roman_string is None:
        return 0
    else:
        return 0
