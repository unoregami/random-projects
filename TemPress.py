import time
import math
import numpy as np

stage = "••••••••••"
stage_value = []
inp = 0

print("===== WELCOME TO TEMPRESS =====")
print("How to play:\nYou get 10 stages. Press ENTER to lock stage time. Each stage needs to have longer time than the previous stage. Smallest deviation, better.")
input("Press anything to start...")
print()

stages_done = 1
for i in range(10):
    print(stage)
    start = time.perf_counter()
    inp = input()
    end = time.perf_counter()
    value = end - start
    stage = stage[:i] + "|" + stage[i+1:]

    if i == 0:
        stage_value.append(value)
        continue
    
    stage_value.append(value)
    if stage_value[i-1] >= value:
        print("GAME OVER")
        break

    stages_done += 1

stage = 0
for i in stage_value:
    stage += 1
    print(f"STAGE {stage}:\t", "|" * math.floor(i*100 / 2))


sd = round(np.std(stage_value), 3)
score = (1-sd) * 100 / (11 - stages_done)   # SD% divided how much stages not done
score += score * (3 - stage_value[-1])  # multiplier. how short the time it took.
print()
print(f"SCORE: {score:.2f}")
print("SD:", sd)
