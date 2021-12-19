from collections import Counter

# a = "cde"
# b = "abc"

def makeAnagram(a, b):
    a_dict = Counter(a)
    b_dict = Counter(b)

    deleted_characters = 0
    
    missing_letters = set(a_dict) ^ set(b_dict)

    for letter in missing_letters:
        try:
            freq = a_dict[letter]
            deleted_characters += freq
        except KeyError:
            pass
        
        try:
            freq = b_dict[letter]
            deleted_characters += freq
        except KeyError:
            pass
    
    overlapping_letters = set(a_dict) & set(b_dict)

    for letter in overlapping_letters:
        freq_a = a_dict[letter]
        freq_b = b_dict[letter]        
        if freq_a != freq_b:
            deletions = abs(freq_a - freq_b)
            deleted_characters += deletions

    return deleted_characters


if __name__ == '__main__':
    a = input()
    b = input()

    result = makeAnagram(a, b)
    print(result)
