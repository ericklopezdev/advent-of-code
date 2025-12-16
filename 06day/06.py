import math

def parse_data(path_file): 
    matrix_data = []
    operators = []
    try:
        with open(path_file, "r") as f:
            all_lines = [row.strip() for row in f.readlines() if row.strip()]
            # last line are the operators
            operator_line = all_lines[-1]
            # split operators
            operators = operator_line.split()
            # the rest of the lines are the matrix data
            matrix_lines = all_lines[:-1]
            for line in matrix_lines:
                try:
                    row_of_ints = [int(n) for n in line.split()]
                    matrix_data.append(row_of_ints)
                except ValueError:
                    print(f"[warning] row has not integer values: {line}")
    except Exception as e:
        print(f"[error]: {e}")
        return None, None
    return matrix_data, operators

def transform_matrix_cols(matrix_data):
    cols = [list(col) for col in zip(*matrix_data)]
    return cols

def operate_sign(cols, operators):
    results = {}
    # i as col position to check the corresponding operator
    for i, col in enumerate(cols):
        sign = operators[i]
        col_name = f"col: {i}_{sign}"
        if sign == '+':
            results[col_name] = sum(col)
        elif sign == '*':
            results[col_name] = math.prod(col)
        else:
            print(f"[todo] unhandled operator '{sign}' in column {i}.")
            results[col_name] = col
    final_sum = 0
    for value in results.values():
        if isinstance(value, (int, float)):
            final_sum += value
    return results, final_sum

PATH_FILE="06.txt"

matrix_data, operators = parse_data(PATH_FILE)
columns = transform_matrix_cols(matrix_data)
result, _sum = operate_sign(columns, operators)

print(_sum)
