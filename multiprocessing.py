from multiprocessing import Process
import time

def count(goal):
    count = 0
    while count < goal:
        count += 1

def process(cores):
    goal = 100000000 // cores
    
    processes = list()
    for _ in range(cores): processes.append(Process(target=count, args=(goal,)))

    start = time.perf_counter()
    for p in processes:
        p.start()
    
    for p in processes:
        p.join()

    end = time.perf_counter()
    print(f"{cores} - Time elapsed:", end - start)


if __name__ == "__main__":
    for i in range(0, 12, 4):
        process(i+4)