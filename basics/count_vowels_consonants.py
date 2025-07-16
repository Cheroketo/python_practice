def count_vowels_consonants(text):
    lst_text = list(text.lower())
    lst_vowel = ['a', 'e', 'o', 'u', 'y', 'i']
    count_vowel = 0
    count_consonant = 0
    for element in lst_text:
        if element.isalpha():
            if element in lst_vowel:
                count_vowel += 1
            else :
                count_consonant += 1
    return count_vowel, count_consonant
print(count_vowels_consonants('abc:frhfbrhbg2651512'))