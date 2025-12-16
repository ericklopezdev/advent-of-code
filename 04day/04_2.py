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
                if grid[ni][nj] == "@":
                    counter += 1
    return counter


def printing_department(path_file):
    try:
        with open(path_file, "r") as file:
            grid = [list(line.strip()) for line in file]

        total_removed = 0

        while True:
            to_remove = []

            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == "@":
                        if can_be_acc(i, j, grid) < 4:
                            to_remove.append((i, j))

            if not to_remove:
                break

            for i, j in to_remove:
                grid[i][j] = "."

            total_removed += len(to_remove)

        print("Total rolls removed:", total_removed)

    except FileNotFoundError:
        print(f"Error: {path_file} not found")

printing_department(PATH_FILE)
