def sort_dict_by_value(d):
    return sorted(d.items(), key=lambda x: x[0], reverse=True)

print(sort_dict_by_value({'a':1, 'b':3, 'c':2}))