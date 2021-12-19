# s = "aabbcd"
# s = "aabbccddeefghi"
# s = "abcdefghhgfedecba"
# s = "aaaabbcc"
# s = "abcdefghhgfedecba"

def isValid(s):
    letter_freqs = {}
    for letter in s:
        try:
            letter_freqs[letter] += 1
        except KeyError:
            letter_freqs[letter] = 1

    freqs = list(letter_freqs.values())
    freqs_freqs = {}
    for freq in freqs:
        try:
            freqs_freqs[freq] += 1
        except KeyError:
            freqs_freqs[freq] = 1    

    if len(freqs_freqs) == 1:
        return "YES"
    elif len(freqs_freqs) > 2:
        return "NO"
    elif 1 in freqs_freqs.values() and (freqs_freqs[min(freqs_freqs.keys())] == 1 or (max(freqs_freqs.keys()) - min(freqs_freqs.keys()) == 1)):
        return "YES"
    else:
        return "NO"


if __name__ == '__main__':
    s = input()
    result = isValid(s)
    print(result)