# 20
# b 3
# a 1
# bb 3
# b 8
# bba 0
# bb 2
# bca 6
# ccc 4
# b 3
# ab 8
# bb 3
# bb 7
# ccb 8
# bbb 2
# aab 8
# b 6
# ab 8
# cb 9
# cbb 8
# ba 9


from functools import cmp_to_key
class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score
        
    def __repr__(self):
        return f"{self.name} {self.score}"
    
    def comparator(a, b):
        if a.score > b.score:
            return -1
        if a.score < b.score:
            return 1
        if a.name < b.name:
            return -1
        return 1
        

n = int(input())
data = []
for i in range(n):
    name, score = input().split()
    score = int(score)
    player = Player(name, score)
    data.append(player)
    
data = sorted(data, key=cmp_to_key(Player.comparator))
for i in data:
    print(i.name, i.score)