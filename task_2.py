import random

# 100 удаа зоос хаяхад сүлд буух магадлал
"""cnt = 0
for i in range(10000):
    if random.random() > 0.5:
        cnt += 1

print(cnt / 10000)"""

# print(random.uniform(1, 5)) # todorhoi range dotor sanamsargui baidlaar too uusgeh ued uniform function iig ashiglaj bolno

# print(random.expovariate(1/3)) # exponential tarhaltiig ilerhiildeg function

# print(random.randrange(10, 101))

# print(random.randrange(3, 1001, 3))

"""deck = list(range(2, 11)) * 4
print(deck)
random.shuffle(deck)
print(deck)
my_deck = []

while True:
    my_deck.append(deck.pop())
    a += deck.pop()
    if a > 19:
        break

while True:
    my_deck.append(deck.pop())
    if sum(my_deck) > 19:
        break
print(my_deck)"""

lottery = ['chinzo', 'james', 'amaraa', 'artyom']

print(random.choice(lottery))