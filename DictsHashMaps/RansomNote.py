
magazine = "give me one grand today night".rstrip().split()
note = "give one grand today".rstrip().split()

def checkMagazine(magazine, note):
    word_menu = {}
    for word in magazine:
        try:
            word_menu[word] += 1
        except:
            word_menu[word] = 1

    for word in note:
        try:
            word_menu[word] -= 1
            if word_menu[word] == 0:
                try:
                    word_menu.pop(word) 
                except KeyError:
                    print("Same key lost between two tries. Should be an impossible scenario")
        except KeyError:
            print("No")
            return

    print("Yes")





if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    n = int(first_multiple_input[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)