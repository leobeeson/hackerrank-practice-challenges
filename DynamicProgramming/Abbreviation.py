import pytest


def abbreviation(a: str, b:str) -> str:
    candidates = set(a)
    for letter in b:
        if letter not in candidates:
            return "NO"


def test_b_has_letters_missing_in_a() -> None:
    a = "AbcDE"
    b = "AFDE"
    result = abbreviation(a, b)
    assert result == "NO"


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

