# s1 = "{[()]}"
# s2 = "{[(])}"
# s3 = "{{[[(())]]}}"

def isBalanced(s):
    stack = []
    for bracket in s:
        if bracket in ["{", "[", "("]:
            stack.append(bracket)
        elif len(stack) == 0:
            return "NO"
        else:
            last = stack[-1]
            if (bracket == "}" and last == "{") or (bracket == "]" and last == "[") or (bracket == ")" and last == "("):
                stack.pop()
            else:
                return "NO"
    if len(stack) == 0:
        return "YES"
    else:
        return "NO"



if __name__ == '__main__':
    t = int(input().strip())
    for t_itr in range(t):
        s = input()
        result = isBalanced(s)
        print(result)