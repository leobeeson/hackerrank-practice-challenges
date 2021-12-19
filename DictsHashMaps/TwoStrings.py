
s1 = "hello"
s2 = "world"
s1 = "hi"
s2 = "world"

def twoStrings(s1, s2):
    memo = {}
    for char in s1:
        try:
            memo[char] = memo[char] +1
        except KeyError:
            memo[char] = 1
    
    for char in s2:
        if char in memo.keys():
            return "YES"
    
    return "NO"



if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s1 = input()
        s2 = input()
        result = twoStrings(s1, s2)
        print(result)