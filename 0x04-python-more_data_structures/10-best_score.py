#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None

    max_key = next(iter(a_dictionary))
    max_value = a_dictionary[max_key]
    for key, value in a_dictionary.items():
        if value > max_value:
            max_value = value
            max_key = key

    return max_key

a_dictionary = {'John': 12, 'Bob': 14, 'Mike': 14, 'Molly': 16, 'Adam': 10}
best_key = best_score(a_dictionary)
print("Best score: {}".format(best_key))

best_key = best_score(None)
print("Best score: {}".format(best_key))


