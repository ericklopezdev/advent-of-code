FILE_PATH='03.txt'

def find_highest_joltage(path_to_file: str)-> int:
    total_joltage = 0

    try:
        with open(path_to_file, 'r') as file:
            lines = file.readlines()
            for line in lines:
                h_n = 0 
                list_str_line = list(line.strip())
                for i in range(len(list_str_line)):
                    for j in range(i + 1, len(list_str_line)):
                        tmp_n = int(list_str_line[i] + list_str_line[j])
                        if tmp_n > h_n:
                            h_n = tmp_n 
                total_joltage += h_n

        print(f"output: {total_joltage}")
        return total_joltage

    except FileNotFoundError:
        print(f"Error: {path_to_file} not found")
        return 0

find_highest_joltage(FILE_PATH)
