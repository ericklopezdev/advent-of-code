FILE_PATH = "03.txt"

def max_joltage_from_line(line: str, k: int = 12) -> int:
    number = line.strip()
    remove = len(number) - k
    stack = []

    for digit in number:
        # remove smaller previous digits while removals are avalable
        while stack and remove > 0 and stack[-1] < digit:
            stack.pop()
            remove -= 1
        stack.append(digit)
    # remove remaining digits from the end to reach required length
    if remove > 0:
        stack = stack[:-remove]

    return int("".join(stack))


def find_total_joltage(path: str) -> int:
    total = 0
    with open(path, "r") as f:
        for line in f:
            total += max_joltage_from_line(line)
    return total


print(find_total_joltage(FILE_PATH))
