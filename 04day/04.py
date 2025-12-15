PATH_FILE="04.txt"

def can_be_acc(i, j, grid):
    counter = 0
    # -1, 0, 1
    for x in range(-1, 2):
        for y in range(-1, 2):
            if x == 0 and y == 0:
                continue
            ni, nj = i + x, j + y
            # boundary check
            if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]):
                position = grid[ni][nj]
                if position == "@":
                    counter += 1
    return counter

def printing_department(path_file):
    try:
        grid = []
        total_accesssible = 0
        with open(path_file, 'r') as file:
            lines = file.readlines()
            grid = [list(line.strip()) for line in lines]

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '@':
                    neighbor_count = can_be_acc(i, j, grid)

                    if neighbor_count < 4:
                        total_accesssible += 1
        print(f"total_accesssible: {total_accesssible}")

    except FileNotFoundError:
        print(f"Error: {path_file} not found")

printing_department(PATH_FILE)
