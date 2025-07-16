def inverted_dict(d):
    inverted = {}
    for key, value in d.items():
        inverted.setdefault(value, []).append(key)
    return inverted

d = {'a': 1, 'b': 1, 'c': 2}
print(inverted_dict(d))
