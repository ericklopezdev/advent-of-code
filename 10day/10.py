import sys

file_path = '10.txt'

def min_presses(target, buttons):
    n = len(target)
    target_mask = 0
    for i in range(n):
        if target[i]:
            target_mask |= (1 << i)
    from collections import deque
    queue = deque([(0, 0)])  # mask, presses
    visited = set([0])
    while queue:
        mask, presses = queue.popleft()
        if mask == target_mask:
            return presses
        for btn in buttons:
            new_mask = mask
            for light in btn:
                new_mask ^= (1 << light)
            if new_mask not in visited:
                visited.add(new_mask)
                queue.append((new_mask, presses + 1))
    return -1

def parse_line(line):
    parts = line.split()
    diagram = parts[0][1:-1]
    buttons_str = parts[1:-1]
    target = [0 if c == '.' else 1 for c in diagram]
    buttons = []
    for b in buttons_str:
        nums = b[1:-1].split(',')
        buttons.append(set(int(x) for x in nums))
    return target, buttons

def main():
    try:
        with open(file_path, 'r') as file:
            lines = file.read().strip().splitlines()
        total_presses = 0
        for line in lines:
            target, buttons = parse_line(line)
            presses = min_presses(target, buttons)
            if presses == -1:
                print("impossible")
                sys.exit(1)
            total_presses += presses
        print(total_presses)
    except FileNotFoundError:
        print(f"[error] file {file_path} not found")

main()
