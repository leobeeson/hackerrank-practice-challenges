import pytest


def candies(num_kids: int, kids_rating: list[int]) -> int:
    num_candies_ranges = [1] * num_kids
    
    if num_kids == 0:
        return 0

    if num_kids == 1:
        return 1

    for idx in range(1, num_kids):
        if kids_rating[idx] > kids_rating[idx - 1]:
            num_candies_ranges[idx] = num_candies_ranges[idx - 1] + 1
        

    for idx in reversed(range(num_kids -1)):
        if (kids_rating[idx] > kids_rating[idx + 1]) and \
            (num_candies_ranges[idx] <= num_candies_ranges[idx + 1]):
            num_candies_ranges[idx] = num_candies_ranges[idx + 1] + 1

    return sum(num_candies_ranges)


@pytest.mark.parametrize(
    "kids_rating,expected_candies_to_buy",
    [
        ([], 0),
        ([42], 1),
        ([4,6,4,5,6,2], 10),
        ([1, 2, 2], 4),
        ([2, 4, 2, 6, 1, 7, 8, 9, 2, 1], 19),
        ([2, 4, 3, 5, 2, 6, 4, 5], 12),
        ([4, 2, 3, 1], 6)
    ]
)
def test_candies(kids_rating, expected_candies_to_buy) -> None:
    candies_to_buy = candies(len(kids_rating), kids_rating)
    assert candies_to_buy == expected_candies_to_buy


if __name__ == "__main__": 
    n = int(input().strip())
    arr = []
    for _ in range(n):
        item = int(input().strip())
        arr.append(item)

    candies_to_buy = candies(n, arr)
