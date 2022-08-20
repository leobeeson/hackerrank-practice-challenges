

def abbreviation(a: str, b:str) -> str:
    pass



if __name__ == '__main__':
    num_queries = int(input().strip())

    for query in range(num_queries):
        a = input()
        b = input()
        result = abbreviation(a, b)
        print(result + "\n")



# Examples

# AbcDE
# ABDE
# Answer: Yes

# AbcDE
# AFDE
# Answer: No

# daBcd
# ABC
# Answer: yes

