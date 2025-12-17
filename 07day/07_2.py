def parse_data(path_file):
    try:
        with open(path_file, "r") as f:
            return [line.strip() for line in f]
    except FileNotFoundError:
        print(f"[error] {path_file} not found")
        return None

def check_splits(cols, line):
    new_cols = {}
    line_len = len(line)
    display_line = list(line)

    for col, count in cols.items():
        char = line[col]
        if char == "^":
            for move in [-1, 1]:
                new_col = col + move
                if 0 <= new_col < line_len:
                    new_cols[new_col] = new_cols.get(new_col, 0) + count
                    display_line[new_col] = "|"
        else:
            new_cols[col] = new_cols.get(col, 0) + count
            display_line[col] = "|"

    return new_cols

def init_simulation(matrix):
    start_col = matrix[0].index("S")
    current_cols = {start_col: 1}

    for line in matrix:
        current_cols = check_splits(current_cols, line)

    total_timelines = sum(current_cols.values())
    print(f"\ntotal timelines reaching the end: {total_timelines}")
    return total_timelines

FILE_PATH = "07.txt"
matrix = parse_data(FILE_PATH)
init_simulation(matrix)
