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
                # break at first match found
                break
    return total_matches 

def total_fresh_ingredients(ranges):
    # sort from lowest to highest ranges
    sorted_ranges = sorted(ranges, key=lambda x: x[0])

    merged_ranges = []
    current_start, current_end = sorted_ranges[0]

    # merge overlapping or adjacent ranges
    for next_start, next_end in sorted_ranges[1:]:
        # next range starts before or adjacent to current end
        if next_start <= current_end + 1:
            # extend the current range end
            current_end = max(current_end, next_end)
        else:
            merged_ranges.append((current_start, current_end))
            current_start, current_end = next_start, next_end

    # add the last merged range
    merged_ranges.append((current_start, current_end))

    # sum the lengths of the merged ranges
    total_count = sum(end - start + 1 for start, end in merged_ranges)
    return total_count

PATH="05.txt"
ranges, numbers = parse_data(PATH)
result = check_worthy(ranges,numbers)
total = total_fresh_ingredients(ranges)
print(total)

