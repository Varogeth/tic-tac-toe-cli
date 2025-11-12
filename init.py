a = 1
b = 2
c = 3
d = 4
e = 5
f = 6
g = 7
h = 8
i = 9

uhh = f"   |   |   "
top = f" {a} | {b} | {c} "
mid = f" {d} | {e} | {f} "
bot = f" {g} | {h} | {i} "
div = f"---|---|---"

game_board = [top, div, mid, div, bot]

for row in game_board:
    print(row)