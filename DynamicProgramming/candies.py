

def candies(num_kids: int, kids_rating: list[int]) -> int:
    pass


if __name__ == "__main__": 
    n = int(input().strip())
    arr = []
    for _ in range(n):
        item = int(input().strip())
        arr.append(item)

    candies_to_buy = candies(n, arr)
