import pytest


def initialise_2d_string_array(a: str, b:str) -> list[list]:
    n = len(a)
    m = len(b)
    string_2d_array = [[False] * (m + 1) for _ in range(n + 1)]
    string_2d_array[0][0] = True
    for i, a_letter in enumerate(a):
        if a_letter.islower():
            string_2d_array[i + 1][0] = True
        else:
            break
    return string_2d_array


def abbreviation(a: str, b:str) -> str:    
    if len(set(b.upper()).difference(set(a.upper()))) > 0:
        return "NO"

    string_2d_array = initialise_2d_string_array(a, b)

    for j in range(1, len(b) + 1):
        b_letter = b[j -1]
        for i in range(1, len(a) + 1):
            a_letter = a[i - 1]
            previous_result = string_2d_array[i - 1][j - 1]
            if a_letter.isupper():
                if previous_result:
                    string_2d_array[i][j] = a_letter == b_letter
            else:
                above_result = string_2d_array[i - 1][j]
                if a_letter.upper() == b_letter:
                    string_2d_array[i][j] = previous_result or above_result
                else:
                    string_2d_array[i][j] = above_result
    result = "YES" if string_2d_array[-1][-1] else "NO"
    return result
                

# TESTS
@pytest.mark.parametrize(
    "a,b,expected",
    [("AbcDE", "AFDE", "NO"), ("daBcd", "ABDE", "NO")]
)
def test_b_has_letters_missing_in_a(a, b, expected) -> None:
    result = abbreviation(a, b)
    assert result == expected


@pytest.mark.parametrize(
    "a,b,expected",
    [
        ("ab", "AB", [True, True, True]), 
        ("aB", "AB", [True, True, False]),
        ("Ab", "AB", [True, False, False])
    ]
)
def test_Bs_empty_string_column_has_true_for_As_lower_cased_letters_from_start(a, b, expected) -> None:   
    string_2d_array = initialise_2d_string_array(a, b)
    empty_string_column = [row[0] for row in string_2d_array]
    assert empty_string_column == expected


@pytest.mark.parametrize(
    "a,b,expected",
    [
        ("AbcDE", "ABDE", "YES"),
        ("AbcDE", "AFDE", "NO"),
        ("daBcd", "ABC", "YES")
    ]
)
def test_abbreviation_function(a, b, expected) -> None:
    result = abbreviation(a, b)
    assert result == expected


# Resources: https://www.youtube.com/watch?v=4WzCFTmjKu4&ab_channel=GlitchedFailure

if __name__ == '__main__':
    num_queries = int(input().strip())

    for query in range(num_queries):
        a = input()
        b = input()
        result = abbreviation(a, b)
        print(result + "\n")


