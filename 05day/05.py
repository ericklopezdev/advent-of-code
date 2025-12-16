
def parse_data(file_path):
    ranges, numbers = [], []
    try:
        with open(file_path, "r") as f:
            parsed_elements = list(f.read().strip().split())
            for element in parsed_elements:
                try:
                    numbers.append(int(element))
                except ValueError:
                    if "-" in element:
                        start_str, end_str = element.split("-")
                        try:
                            ranges.append((int(start_str), int(end_str)))
                        except ValueError:
                            print(f"[warning] malformed range {element}")
                    else:
                        print(f"[warning] unhandled element {element}")
            return ranges, numbers
    except FileNotFoundError:
        print(f"[error] file {file_path} not found")
        return [], []

# check if n is in x-range
def is_fresh(_range, number):
    start, end = _range
    if start <= number <= end:
        return True
    return False

def check_worthy(ranges, numbers):
    total_matches = 0
    for number in numbers:
        matches = []
        for _range in ranges:
            if is_fresh(_range, number):
                range_str = f"{_range[0]}-{_range[1]}"
                matches.append(range_str)
                total_matches += 1
                print(f"match: {_range}, {number}")
                # break at first match found
                break
    return total_matches 

PATH="05.txt"
ranges, numbers = parse_data(PATH)
print(ranges, numbers)
result = check_worthy(ranges,numbers)
print(result)
