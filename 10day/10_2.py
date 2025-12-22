import pulp

def fewest_presses(options, goal):
    num_buttons = len(options)
    num_counters = len(goal)
    problem = pulp.LpProblem("FactoryMachine", pulp.LpMinimize)
    presses = [pulp.LpVariable(f"press_{j}", lowBound=0, cat="Integer") for j in range(num_buttons)]
    problem += pulp.lpSum(presses)
    for counter in range(num_counters):
        problem += pulp.lpSum(presses[j] for j, btn in enumerate(options) if counter in btn) == goal[counter]
    problem.solve(pulp.PULP_CBC_CMD(msg=0))
    if pulp.LpStatus[problem.status] != "Optimal":
        raise ValueError(f"No solution found for goal = {goal}")
    return sum(int(p.varValue) for p in presses)


def parse_line(line):
    parts = line.split()
    button_parts = parts[1:-1]
    buttons = []
    for part in button_parts:
        indices = part[1:-1].split(',')
        indices = [int(x) for x in indices if x]
        buttons.append(tuple(indices))
    targets = [int(x) for x in parts[-1][1:-1].split(',')]
    return (targets, buttons)


def main():
    total_presses = 0
    with open('10.txt') as file:
        for machine_num, line in enumerate(file, start=1):
            line = line.strip()
            if not line:
                continue
            targets, buttons = parse_line(line)
            presses = fewest_presses(buttons, targets)
            print(f"Machine {machine_num}: goal={targets} → presses={presses}")
            total_presses += presses
    print("minimal presses:", total_presses)


main()
