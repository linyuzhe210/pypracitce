import random
cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
color = ['Diamond', 'Heart', 'Plum', 'Spade']

ls = []
poke = ['Joker', 'joker']
for j in color:
    for n in cards:
        ls.append(j + ' ' + n)

ls += poke
poke = random.sample(ls, 3)
ls = list(set(ls) - set(poke))
random.shuffle(ls)
player_a = []
player_b = []
player_c = []
for index in range(len(ls)):
    ls_map = ls[index]
    if index % 3 == 0:
        player_a.append(ls_map)
    elif index % 3 == 1:
        player_b.append(ls_map)
    else:
        player_c.append(ls_map)

print(player_a)
print(player_b)
print(player_c)
print(poke)