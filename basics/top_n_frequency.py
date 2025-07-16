def top_n_frequency(lst, n):
    dict_freq = {}
    for element in lst:
        if element in dict_freq:
            dict_freq[element] += 1
        else:
            dict_freq[element] = 1
    sorted_dict_freq = dict(sorted(dict_freq.items(), key=lambda x: x[1], reverse=True))
    return [key for key, _ in sorted_dict_freq.items()][:n]
print(top_n_frequency([1,1,2,2,2,3], 2))