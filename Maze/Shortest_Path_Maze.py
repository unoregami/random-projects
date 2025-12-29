import random
import numpy as np
import matplotlib.pyplot as plt
import time
import heapq
import os


def create_maze(dim, seed=42):
    # Initialize random seed
    random.seed(seed)
    # Create a grid filled with walls
    maze = np.ones((dim * 2 + 1, dim * 2 + 1))
    # Define the starting point
    x, y = (0, 0)
    maze[2 * x + 1, 2 * y + 1] = 0
    # Initialize the stack with the starting point
    stack = [(x, y)]
    while len(stack) > 0:
        x, y = stack[-1]
        # Define possible directions
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        random.shuffle(directions)

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if nx >= 0 and ny >= 0 and nx < dim and ny < dim:
                if maze[2 * nx + 1, 2 * ny + 1] == 1:
                    maze[2 * nx + 1, 2 * ny + 1] = 0
                    maze[2 * x + 1 + dx, 2 * y + 1 + dy] = 0
                    stack.append((nx, ny))
                    break
        else:
            stack.pop()

    # Create an entrance and an exit
    maze[1, 0] = 0
    maze[-2, -1] = 0
    random.seed(None)
    return maze

def create_imperfect_maze(dim, seed=42, extra_wall_removals=0.05):
    maze = create_maze(dim, seed)

    wall_candidates = []
    for i in range(1, maze.shape[0] - 1):
        for j in range(1, maze.shape[1] - 1):
            if maze[i, j] == 1:
                if maze[i - 1, j] == 0 and maze[i + 1, j] == 0:
                    wall_candidates.append((i, j))
                elif maze[i, j - 1] == 0 and maze[i, j + 1] == 0:
                    wall_candidates.append((i, j))

    num_to_remove = int(len(wall_candidates) * extra_wall_removals)
    walls_to_remove = random.sample(wall_candidates, num_to_remove)
    for i, j in walls_to_remove:
        maze[i, j] = 0

    return maze

def displayMaze(maze):
    if type(maze) == np.ndarray:    # displays numpy maze
        for i in maze:
            for j in range(len(i)):
                if i[j] == 1:
                    print("■", end=" ")
                else:
                    print(" ", end=" ")
            print()
    elif type(maze) == str:         # display maze from files
        for i in maze:
            if i == "1":
                print("■", end=" ")
            elif i == "0":
                print(" ", end=" ")
            elif i == "\n":
                print()
            else:
                continue

def exportMaze(maze: np.ndarray):   # exports bare num maze to text file
    fileName = input("File: ")
    maze_type = input("1 - Dot maze | 2 - Num maze")
    
    match maze_type:
        case "1":
            # Maze in dot form
            maze_output = toDot(maze)
        case "2":
            # Converts maze to bare numbers
            maze_output = toBareMaze(maze)
    
    with open(f"Maze/Perfect/Easy/{fileName}.txt", "a") as f:
        f.write(str(maze_output))
    
    print("Done")

def generateMazes():    # automates generation of 30k mazes
    results = ""
    for i in range(2): # Perfect/Imperfect
        if i == 0:  # Perfect
            start = time.perf_counter()

            for j in range(15000):
                print(j)
                seed = random.random()
                seedName = str(int(round(seed, 10) * 10000000000))

                if j < 5000:    # Easy
                    fileName = "Easy" + seedName
                    maze = create_maze(10, seed)
                    maze = toBareMaze(maze)
                    with open(f"Maze/Perfect/Easy/{fileName}.txt", "a") as f:
                        f.write(str(maze))
                elif j < 10000: # Medium
                    fileName = "Medium" + seedName
                    maze = create_maze(36, seed)
                    maze = toBareMaze(maze)
                    with open(f"Maze/Perfect/Medium/{fileName}.txt", "a") as f:
                        f.write(str(maze))
                else:           # Hard
                    fileName = "Hard" + seedName
                    maze = create_maze(50, seed)
                    maze = toBareMaze(maze)
                    with open(f"Maze/Perfect/Hard/{fileName}.txt", "a") as f:
                        f.write(str(maze))
        else:   # Imperfect
            end = time.perf_counter()
            results += f"Generated perfect mazes: {end - start}\n"
            start = time.perf_counter()

            for j in range(15000):
                print(j)
                seed = random.random()
                seedName = str(int(round(seed, 10) * 10000000000))

                if j < 5000:    # Easy
                    fileName = "Easy" + seedName
                    maze = create_imperfect_maze(10, seed)
                    maze = toBareMaze(maze)
                    with open(f"Maze/Imperfect/Easy/{fileName}.txt", "a") as f:
                        f.write(str(maze))
                elif j < 10000: # Medium
                    fileName = "Medium" + seedName
                    maze = create_imperfect_maze(36, seed)
                    maze = toBareMaze(maze)
                    with open(f"Maze/Imperfect/Medium/{fileName}.txt", "a") as f:
                        f.write(str(maze))
                else:           # Hard
                    fileName = "Hard" + seedName
                    maze = create_imperfect_maze(50, seed)
                    maze = toBareMaze(maze)
                    with open(f"Maze/Imperfect/Hard/{fileName}.txt", "a") as f:
                        f.write(str(maze))

            end = time.perf_counter()
            results += f"Generated imperfect mazes: {end -start}"
            "tres"
        
        print(results)

def toDot(maze):    # returns "." version of maze
    output = ""

    for i in maze:
        for j in range(len(i)):
            if i[j] == 1:
                output += "."
            else:
                output += " "
            output += " "
        output += "\n"
    
    return output

def toBareMaze(maze):    # returns bare num maze
    maze_bare = ""
    for i in maze:
        for j in i:
            maze_bare += f"{int(j)}"
        maze_bare += "\n"
    
    return maze_bare

def isMazeUnique(mazeA, mazeB): # validates two mazes if they are unique
    for i in range(len(mazeA)):
        for j in range(len(mazeA[0])):
            if mazeA[i][j] != mazeB[i][j]:
                return True
            "uno"
    return False

def normalizeMaze(maze):    # to np ndarray
    maze_array = []
    ph = []
    for letter in maze:
        if letter == "\n":
            maze_array.append(ph.copy())
            ph.clear()
            continue
        ph.append(int(letter))
    maze = np.asarray(maze_array, dtype=np.float32)

    return maze

def draw_maze(maze, path=None): # displays maze in a pyplot
    fig, ax = plt.subplots(figsize=(8,8))
    
    # Set the border color to white
    fig.patch.set_edgecolor('white')
    fig.patch.set_linewidth(0)

    if type(maze) != np.ndarray:
        # Normalize maze to np.ndarray
        maze = normalizeMaze(maze)

    ax.imshow(maze, cmap=plt.cm.binary, interpolation='nearest')
    
    # Draw the solution path if it exists
    if path is not None:
        x_coords = [x[1] for x in path]
        y_coords = [y[0] for y in path]
        ax.plot(x_coords, y_coords, color='red', linewidth=2)
    
    ax.set_xticks([])
    ax.set_yticks([])    
    plt.show()

def dijkstra(maze, start, goal):
    rows, cols = len(maze), len(maze[0])
    distances = [[float('inf')] * cols for _ in range(rows)]
    distances[start[0]][start[1]] = 0
    visited = [[False] * cols for _ in range(rows)]
    heap = [(0, start, [start])]  # (cost, (x, y), path)

    def in_bounds(x, y):
        return 0 <= x < rows and 0 <= y < cols

    while heap:
        cost, (x, y), path = heapq.heappop(heap)
        "dos"

        if visited[x][y]:
            continue
        visited[x][y] = True

        if (x, y) == goal:
            return path

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if in_bounds(nx, ny) and maze[nx][ny] == 0:
                if not visited[nx][ny]:
                    new_cost = cost + 1 
                    if new_cost < distances[nx][ny]:
                        distances[nx][ny] = new_cost
                        heapq.heappush(
                            heap, 
                            (new_cost, (nx, ny), path + [(nx, ny)])
                            )
    return None

def manhattan(a, b):
    """Heuristic: Manhattan distance between two points."""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star(maze, start, goal):
    rows, cols = len(maze), len(maze[0])
    open_set = []
    heapq.heappush(
        open_set, 
        (0 + manhattan(start, goal), 0, start, [start])
        )  # (f, g, cell, path)

    g_scores = [[float('inf')] * cols for _ in range(rows)]
    g_scores[start[0]][start[1]] = 0

    visited = [[False] * cols for _ in range(rows)]

    def in_bounds(x, y):
        return 0 <= x < rows and 0 <= y < cols

    while open_set:
        f, g, current, path = heapq.heappop(open_set)
        x, y = current
        if visited[x][y]:
            continue
        visited[x][y] = True
        if current == goal:
            return path

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy

            if in_bounds(nx, ny) and maze[nx][ny] == 0:
                tentative_g = g + 1  # uniform cost
                if tentative_g < g_scores[nx][ny]:
                    g_scores[nx][ny] = tentative_g
                    f_score = tentative_g + manhattan((nx, ny), goal)
                    heapq.heappush(
                        open_set, 
                        (f_score, tentative_g, (nx, ny), path + [(nx, ny)])
                        )

    return None

def runTest():  # run simulation to maze dataset
    results = {
        "perfect": {
            "easy": {
                "ast": {
                    "time": [],
                    "score": 0
                },
                "dij": {
                    "time": [],
                    "score": 0
                }
            },
            "medium": {
                "ast": {
                    "time": [],
                    "score": 0
                },
                "dij": {
                    "time": [],
                    "score": 0
                }
            },
            "hard": {
                "ast": {
                    "time": [],
                    "score": 0
                },
                "dij": {
                    "time": [],
                    "score": 0
                }
            }
        },
        "imperfect": {
            "easy": {
                "ast": {
                    "time": [],
                    "score": 0
                },
                "dij": {
                    "time": [],
                    "score": 0
                }
            },
            "medium": {
                "ast": {
                    "time": [],
                    "score": 0
                },
                "dij": {
                    "time": [],
                    "score": 0
                }
            },
            "hard": {
                "ast": {
                    "time": [],
                    "score": 0
                },
                "dij": {
                    "time": [],
                    "score": 0
                }
            }
        }
    }
    
    # Perfect mazes
    for folder in os.listdir(f"Maze\\Perfect"):
        for maze_name in os.listdir(f"Maze\\Perfect\\{folder}"):
            with open(f"Maze\\Perfect\\{folder}\\{maze_name}") as f:
                maze = f.read()
                maze = normalizeMaze(maze)
                start = (1, 0)
                end = (maze.shape[0]-2, maze.shape[1]-1)

                # Dijkstra
                time_start = time.perf_counter()
                maze_path = dijkstra(maze, start, end)
                time_end = time.perf_counter()
                dij_time = time_end - time_start

                # A-star
                time_start = time.perf_counter()
                maze_path = a_star(maze, start, end)
                time_end = time.perf_counter()
                ast_time = time_end - time_start

                # Store results
                match folder:
                    case "Easy":
                        results["perfect"]["easy"]["dij"]["time"].append(dij_time)
                        results["perfect"]["easy"]["ast"]["time"].append(ast_time)
                        if dij_time < ast_time:
                            results["perfect"]["easy"]["dij"]["score"] += 1
                        else:
                            results["perfect"]["easy"]["ast"]["score"] += 1
                    case "Medium":
                        results["perfect"]["medium"]["dij"]["time"].append(dij_time)
                        results["perfect"]["medium"]["ast"]["time"].append(ast_time)
                        if dij_time < ast_time:
                            results["perfect"]["medium"]["dij"]["score"] += 1
                        else:
                            results["perfect"]["medium"]["ast"]["score"] += 1
                    case "Hard":
                        results["perfect"]["hard"]["dij"]["time"].append(dij_time)
                        results["perfect"]["hard"]["ast"]["time"].append(ast_time)
                        if dij_time < ast_time:
                            results["perfect"]["hard"]["dij"]["score"] += 1
                        else:
                            results["perfect"]["hard"]["ast"]["score"] += 1
                    case _:
                        print("INVALID FOLDER")
                print(maze_name, len(maze_path))

    # Imperfect mazes
    for folder in os.listdir(f"Maze\\Imperfect"):
        for maze_name in os.listdir(f"Maze\\Imperfect\\{folder}"):
            with open(f"Maze\\Imperfect\\{folder}\\{maze_name}") as f:
                maze = f.read()
                maze = normalizeMaze(maze)
                start = (1, 0)
                end = (maze.shape[0]-2, maze.shape[1]-1)

                # Dijkstra
                time_start = time.perf_counter()
                maze_path = dijkstra(maze, start, end)
                time_end = time.perf_counter()
                dij_time = time_end - time_start

                # A-star
                time_start = time.perf_counter()
                maze_path = a_star(maze, start, end)
                time_end = time.perf_counter()
                ast_time = time_end - time_start

                # Store results
                match folder:
                    case "Easy":
                        results["imperfect"]["easy"]["dij"]["time"].append(dij_time)
                        results["imperfect"]["easy"]["ast"]["time"].append(ast_time)
                        if dij_time < ast_time:
                            results["imperfect"]["easy"]["dij"]["score"] += 1
                        else:
                            results["imperfect"]["easy"]["ast"]["score"] += 1
                    case "Medium":
                        results["imperfect"]["medium"]["dij"]["time"].append(dij_time)
                        results["imperfect"]["medium"]["ast"]["time"].append(ast_time)
                        if dij_time < ast_time:
                            results["imperfect"]["medium"]["dij"]["score"] += 1
                        else:
                            results["imperfect"]["medium"]["ast"]["score"] += 1
                    case "Hard":
                        results["imperfect"]["hard"]["dij"]["time"].append(dij_time)
                        results["imperfect"]["hard"]["ast"]["time"].append(ast_time)
                        if dij_time < ast_time:
                            results["imperfect"]["hard"]["dij"]["score"] += 1
                        else:
                            results["imperfect"]["hard"]["ast"]["score"] += 1
                    case _:
                        print("INVALID FOLDER")
                print(maze_name, len(maze_path))

    return results


if __name__ == "__main__":
    # Open maze file
    with open(f"Maze\Imperfect\Medium\Medium55074519.txt") as f:
        maze = f.read()
        draw_maze(maze)
        maze = normalizeMaze(maze)
        start = (1, 0)
        end = (maze.shape[0]-2, maze.shape[1]-1)
        
    #     # Dijkstra
    #     time_start = time.perf_counter()
    #     maze_path = dijkstra(maze, start, end)
    #     time_end = time.perf_counter()
    #     print(f"Dijkstra: {time_end - time_start:.4f}")
    #     draw_maze(maze, path=maze_path)

    #     # A*
    #     time_start = time.perf_counter()
    #     maze_path = a_star(maze, start, end)
    #     time_end = time.perf_counter()
    #     print(f"A*: {time_end - time_start:.4f}")
    #     draw_maze(maze, path=maze_path)


    # # Auto generate mazes (30k)
    # start = time.perf_counter()
    # generateMazes()
    # end = time.perf_counter()
    # print(f"Done. {end - start}")


    # # Run test simulation
    # results = runTest()
    # print(results)

    # perfect_easy_dij_score = results["perfect"]["easy"]["dij"]["score"]
    # perfect_easy_dij_total_time = sum(results["perfect"]["easy"]["dij"]["time"])
    # perfect_easy_dij_ave_time = perfect_easy_dij_total_time / len(results["perfect"]["easy"]["dij"]["time"])
    # perfect_med_dij_score = results["perfect"]["medium"]["dij"]["score"]
    # perfect_med_dij_total_time = sum(results["perfect"]["medium"]["dij"]["time"])
    # perfect_med_dij_ave_time = perfect_med_dij_total_time / len(results["perfect"]["medium"]["dij"]["time"])
    # perfect_hard_dij_score = results["perfect"]["hard"]["dij"]["score"]
    # perfect_hard_dij_total_time = sum(results["perfect"]["hard"]["dij"]["time"])
    # perfect_hard_dij_ave_time = perfect_hard_dij_total_time / len(results["perfect"]["hard"]["dij"]["time"])

    # perfect_easy_ast_score = results["perfect"]["easy"]["ast"]["score"]
    # perfect_easy_ast_total_time = sum(results["perfect"]["easy"]["ast"]["time"])
    # perfect_easy_ast_ave_time = perfect_easy_ast_total_time / len(results["perfect"]["easy"]["ast"]["time"])
    # perfect_med_ast_score = results["perfect"]["medium"]["ast"]["score"]
    # perfect_med_ast_total_time = sum(results["perfect"]["medium"]["ast"]["time"])
    # perfect_med_ast_ave_time = perfect_med_ast_total_time / len(results["perfect"]["medium"]["ast"]["time"])
    # perfect_hard_ast_score = results["perfect"]["hard"]["ast"]["score"]
    # perfect_hard_ast_total_time = sum(results["perfect"]["hard"]["ast"]["time"])
    # perfect_hard_ast_ave_time = perfect_hard_ast_total_time / len(results["perfect"]["hard"]["ast"]["time"])

    # imperfect_easy_dij_score = results["imperfect"]["easy"]["dij"]["score"]
    # imperfect_easy_dij_total_time = sum(results["imperfect"]["easy"]["dij"]["time"])
    # imperfect_easy_dij_ave_time = imperfect_easy_dij_total_time / len(results["imperfect"]["easy"]["dij"]["time"])
    # imperfect_med_dij_score = results["imperfect"]["medium"]["dij"]["score"]
    # imperfect_med_dij_total_time = sum(results["imperfect"]["medium"]["dij"]["time"])
    # imperfect_med_dij_ave_time = imperfect_med_dij_total_time / len(results["imperfect"]["medium"]["dij"]["time"])
    # imperfect_hard_dij_score = results["imperfect"]["hard"]["dij"]["score"]
    # imperfect_hard_dij_total_time = sum(results["imperfect"]["hard"]["dij"]["time"])
    # imperfect_hard_dij_ave_time = imperfect_hard_dij_total_time / len(results["imperfect"]["hard"]["dij"]["time"])

    # imperfect_easy_ast_score = results["imperfect"]["easy"]["ast"]["score"]
    # imperfect_easy_ast_total_time = sum(results["imperfect"]["easy"]["ast"]["time"])
    # imperfect_easy_ast_ave_time = imperfect_easy_ast_total_time / len(results["imperfect"]["easy"]["ast"]["time"])
    # imperfect_med_ast_score = results["imperfect"]["medium"]["ast"]["score"]
    # imperfect_med_ast_total_time = sum(results["imperfect"]["medium"]["ast"]["time"])
    # imperfect_med_ast_ave_time = imperfect_med_ast_total_time / len(results["imperfect"]["medium"]["ast"]["time"])
    # imperfect_hard_ast_score = results["imperfect"]["hard"]["ast"]["score"]
    # imperfect_hard_ast_total_time = sum(results["imperfect"]["hard"]["ast"]["time"])
    # imperfect_hard_ast_ave_time = imperfect_hard_ast_total_time / len(results["imperfect"]["hard"]["ast"]["time"])

    # print("=" * 50)
    # print("PERFECT MAZES")
    # print("Dijkstra")
    # print(f"Easy:\n\tScore: {perfect_easy_dij_score}\n\tTotal Time: {perfect_easy_dij_total_time}sec\n\tAve Time: {perfect_easy_dij_ave_time}")
    # print(f"Medium:\n\tScore: {perfect_med_dij_score}\n\tTotal Time: {perfect_med_dij_total_time}sec\n\tAve Time: {perfect_med_dij_ave_time}")
    # print(f"Hard:\n\tScore: {perfect_hard_dij_score}\n\tTotal Time: {perfect_hard_dij_total_time}sec\n\tAve Time: {perfect_hard_dij_ave_time}")
    # print()
    # print("A-star")
    # print(f"Easy:\n\tScore: {perfect_easy_ast_score}\n\tTotal Time: {perfect_easy_ast_total_time}sec\n\tAve Time: {perfect_easy_ast_ave_time}")
    # print(f"Medium:\n\tScore: {perfect_med_ast_score}\n\tTotal Time: {perfect_med_ast_total_time}sec\n\tAve Time: {perfect_med_ast_ave_time}")
    # print(f"Hard:\n\tScore: {perfect_hard_ast_score}\n\tTotal Time: {perfect_hard_ast_total_time}sec\n\tAve Time: {perfect_hard_ast_ave_time}")
    # print("=" * 50)
    # print("IMPERFECT MAZES")
    # print("Dijkstra")
    # print(f"Easy:\n\tScore: {imperfect_easy_dij_score}\n\tTotal Time: {imperfect_easy_dij_total_time}sec\n\tAve Time: {imperfect_easy_dij_ave_time}")
    # print(f"Medium:\n\tScore: {imperfect_med_dij_score}\n\tTotal Time: {imperfect_med_dij_total_time}sec\n\tAve Time: {imperfect_med_dij_ave_time}")
    # print(f"Hard:\n\tScore: {imperfect_hard_dij_score}\n\tTotal Time: {imperfect_hard_dij_total_time}sec\n\tAve Time: {imperfect_hard_dij_ave_time}")
    # print()
    # print("A-star")
    # print(f"Easy:\n\tScore: {imperfect_easy_ast_score}\n\tTotal Time: {imperfect_easy_ast_total_time}sec\n\tAve Time: {imperfect_easy_ast_ave_time}")
    # print(f"Medium:\n\tScore: {imperfect_med_ast_score}\n\tTotal Time: {imperfect_med_ast_total_time}sec\n\tAve Time: {imperfect_med_ast_ave_time}")
    # print(f"Hard:\n\tScore: {imperfect_hard_ast_score}\n\tTotal Time: {imperfect_hard_ast_total_time}sec\n\tAve Time: {imperfect_hard_ast_ave_time}")
    # print("=" * 50)


    # # Single maze simulation test
    # maze = create_imperfect_maze(20, random.random())
    # displayMaze(maze)
    # start = (1, 0)
    # end = (maze.shape[0]-2, maze.shape[1]-1)

    # # A-star
    # time_start = time.perf_counter()
    # maze_path = a_star(maze, start, end)
    # time_end = time.perf_counter()
    # print(len(maze_path), f"{time_end - time_start:.4f}")
    # draw_maze(maze, path=maze_path)

    # # Dijkstra
    # time_start = time.perf_counter()
    # maze_path = dijkstra(maze, start, end)
    # time_end = time.perf_counter()
    # print(len(maze_path), f"{time_end - time_start:.4f}")
    # draw_maze(maze, path=maze_path)


    # Increasing maze dimensions test
    score = [0, 0]
    ast_time = []
    dij_time = []
    for i in range(10, 510, 10):
        maze = create_imperfect_maze(i, random.random())
        start = (1, 0)
        end = (maze.shape[0]-2, maze.shape[1]-1)
        print(i)

        # A-star
        time_start = time.perf_counter()
        maze_path = a_star(maze, start, end)
        time_end = time.perf_counter()
        a_time = time_end - time_start
        ast_time.append(a_time)
        print(f"A-Star: {a_time:.4f}")

        # Dijkstra
        time_start = time.perf_counter()
        maze_path = dijkstra(maze, start, end)
        time_end = time.perf_counter()
        dijkstra_time = time_end - time_start
        dij_time.append(dijkstra_time)
        print(f"Dijkstra: {dijkstra_time:.4f}")

        if a_time < dijkstra_time:
            score[0] += 1
        else:
            score[1] += 1
    
    print("=" * 50)
    print("A-star:")
    print(f"\tScore: {score[0]}")
    print(f"\tTotal Time: {sum(ast_time)}")
    print(f"\tAve Time: {sum(ast_time) / len(ast_time)}")
    print("=" * 50)
    print("Dijkstra's:")
    print(f"\tScore: {score[1]}")
    print(f"\tTotal Time: {sum(dij_time)}")
    print(f"\tAve Time: {sum(dij_time) / len(dij_time)}")


    # # 15k Perfect Mazes test
    # score = [0, 0]
    # simulation_time_start = time.perf_counter()
    # for i in range(15000):
    #     if i < 5000:    # Easy
    #         maze_title = "Easy"
    #         maze = create_maze(10, random.random())
    #         start = (1,0)
    #         end = (maze.shape[0]-2, maze.shape[1]-1)
    #     elif i < 10000: # Medium
    #         maze_title = "Medium"
    #         maze = create_maze(36, random.random())
    #         start = (1,0)
    #         end = (maze.shape[0]-2, maze.shape[1]-1)
    #     else:           # Hard
    #         maze_title = "Hard"
    #         maze = create_maze(50, random.random())
    #         start = (1,0)
    #         end = (maze.shape[0]-2, maze.shape[1]-1)

    #     print(maze_title)
    #     # Dijkstra
    #     time_start = time.perf_counter()
    #     maze_path = dijkstra(maze, start, end)
    #     time_end = time.perf_counter()
    #     dijkstra_time = time_end - time_start
    #     print(f"Dijkstra: {dijkstra_time:.4f}")

    #     # A*
    #     time_start = time.perf_counter()
    #     maze_path = a_star(maze, start, end)
    #     time_end = time.perf_counter()
    #     a_star_time = time_end - time_start
    #     print(f"A*: {a_star_time:.4f}")

    #     if a_star_time < dijkstra_time:
    #         score[0] += 1
    #     else:
    #         score[1] += 1

    # simulation_time_end = time.perf_counter()
    # simulation_time = simulation_time_end - simulation_time_start

    # print("=" * 100)
    # print(f"A-star: {score[0]}\t|\tDijkstra: {score[1]}")
    # print(f"Simulation Time: {simulation_time:.4f}")
    # print("=" * 100)

    # # 15k Imperfect Mazes test
    # score = [0, 0]
    # simulation_time_start = time.perf_counter()
    # for i in range(15000):
    #     if i < 5000:    # Easy
    #         maze_title = "Easy"
    #         maze = create_imperfect_maze(10, random.random())
    #         start = (1,0)
    #         end = (maze.shape[0]-2, maze.shape[1]-1)
    #     elif i < 10000: # Medium
    #         maze_title = "Medium"
    #         maze = create_imperfect_maze(36, random.random())
    #         start = (1,0)
    #         end = (maze.shape[0]-2, maze.shape[1]-1)
    #     else:           # Hard
    #         maze_title = "Hard"
    #         maze = create_imperfect_maze(50, random.random())
    #         start = (1,0)
    #         end = (maze.shape[0]-2, maze.shape[1]-1)

    #     print(maze_title)
    #     # Dijkstra
    #     time_start = time.perf_counter()
    #     maze_path = dijkstra(maze, start, end)
    #     time_end = time.perf_counter()
    #     dijkstra_time = time_end - time_start
    #     print(f"Dijkstra: {dijkstra_time:.4f}")

    #     # A*
    #     time_start = time.perf_counter()
    #     maze_path = a_star(maze, start, end)
    #     time_end = time.perf_counter()
    #     a_star_time = time_end - time_start
    #     print(f"A*: {a_star_time:.4f}")

    #     if a_star_time < dijkstra_time:
    #         score[0] += 1
    #     else:
    #         score[1] += 1
    # simulation_time_end = time.perf_counter()
    # simulation_time = simulation_time_end - simulation_time_start

    # print("=" * 100)
    # print(f"A-star: {score[0]}\t|\tDijkstra: {score[1]}")
    # print(f"Simulation Time: {simulation_time:.4f}")
    # print("=" * 100)