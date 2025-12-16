import math
from itertools import zip_longest

def parse_data(path_file): 
    matrix_data = []
    operators = []
    try:
        with open(path_file, "r") as f:
            all_lines = [row.strip() for row in f.readlines() if row.strip()]
            if not all_lines: return None, None
            # last line are the operators
            # split operators
            operators = all_lines[-1].split()
            # the rest of the lines are the matrix data
            matrix_lines = all_lines[:-1]
            for line in matrix_lines:
                # keep str instead of casting them to int
                matrix_data.append(line.split())
    except Exception as e:
        print(f"[error]: {e}")
        return None, None
    return matrix_data, operators

def transform_matrix_cols(matrix_data):
    return [list(col) for col in zip(*matrix_data)]

def get_cols_from_col(col):
    # revers each number
    reversed_strings = [s[::-1] for s in col]
    vertical_groups = zip_longest(*reversed_strings, fillvalue='')
    result = [int("".join(group)) for group in vertical_groups if any(group)]
    return result

def operate_sign(cols, operators):
    results = {}
    final_total_sum = 0
    # i as col position to check the corresponding operator
    for i, col in enumerate(cols):
        sign = operators[i]
        col_name = f"col_{i}_{sign}"
        transformed_numbers = get_cols_from_col(col)
        if sign == '+':
            col_result = sum(transformed_numbers)
        elif sign == '*':
            col_result = math.prod(transformed_numbers)
        else:
            col_result = 0
        results[col_name] = col_result
        final_total_sum += col_result
    return results, final_total_sum

PATH_FILE = "06.txt"

matrix_data, operators = parse_data(PATH_FILE)
columns = transform_matrix_cols(matrix_data)
detailed_results, total = operate_sign(columns, operators)

print(f"total: {total}")
