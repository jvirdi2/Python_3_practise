from functools import cmp_to_key
class Player:
    def __init__(self,name, score):
        self.name = name
        self.score = score
    def __repr__(self):
        pass
    def comparator(self, b):
        val = b.score - self.score
        if val == 0:
            return -1 if self.name < b.name else 1
        return val
        
n = int(input())
data = []
for i in range(n):
    name, score = input().split()
    score = int(score)
    player = Player(name, score)
    data.append(player)

print (data)
    
data = sorted(data, key=cmp_to_key(Player.comparator))
for i in data:
    print(i.name, i.score)

