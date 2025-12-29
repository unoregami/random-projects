import time
import random

w, h = 25, 25
sc = []

def update(screen:list):     # display the screen
    for row in screen:
        for cell in row:
            print(cell, end=" ")
        print()
    print()

def spread(screen:list):
    col_len = len(screen)
    screen_copy = [row[:] for row in screen]
    for y in range((col_len-1), -1, -1):
        for x in range(len(screen[y])):
            cell = screen[y][x]
            if cell == 0:
                continue

            spread_val = cell - 1        #round((col_len / y * cell) - cell)
            spread_val = max(0, spread_val)
            # update adjacent cells based on chance
            try:
                chance = round(random.random() + 0.1)
                if not screen_copy[y][x-1] and chance: screen_copy[y][x-1] = spread_val # left
                # if not screen_copy[y-1][x-1]: screen_copy[y-1][x-1] = spread_val
                chance = round(random.random() + 0.1)
                if not screen_copy[y-1][x] and chance: screen_copy[y-1][x] = spread_val # top
                # if not screen_copy[y-1][x+1]: screen_copy[y-1][x+1] = spread_val
                chance = round(random.random() + 0.1)
                if not screen_copy[y][x+1] and chance: screen_copy[y][x+1] = spread_val # right
                chance = round(random.random() + 0.1)
                if not screen_copy[y+1][x] and chance: screen_copy[y+1][x] = spread_val
            except:
                pass
        
    return screen_copy
        


for _ in range(w):
    ph = []
    for _ in range(h):
        ph.append(0)
    sc.append(ph)

sc[5][7] = 50

for i in range(20):
    time.sleep(1)
    update(sc)
    sc = spread(sc)