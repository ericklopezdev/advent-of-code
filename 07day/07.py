def parse_data(path_file):
    try:
        with open(path_file, "r") as f:
            matrix = [list(line.strip()) for line in f.readlines()]
        return matrix
    except FileNotFoundError:
        print(f"[error] {path_file} not found")
        return None

def check_splits(line):
    # check by lines if the beans has its own col 
    # if it does not, shouldn't to be count
    # find the S to start
    # goes downward until find splitter ^
    # could use a num list position of col to go down
    # avoid overflowing list
    return False, None

def init_simulation(matrix):
    ans = 0
    for line in matrix:
        was_splited, last_cols = check_splits(line)
    return ans

FILE_PATH = "07.txt"
matrix = parse_data(FILE_PATH)
init_simulation(matrix)
