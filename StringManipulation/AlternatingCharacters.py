

def alternatingCharacters(s):
    deletions = 0
    if len(s) < 2:
        return deletions

    current_letter = ""
    for letter in s:
        if letter != current_letter:
            current_letter = letter
        else:
            deletions += 1

    return deletions


if __name__ == '__main__':
    q = int(input().strip())
    for q_itr in range(q):
        s = input()
        result = alternatingCharacters(s)
        print(result)