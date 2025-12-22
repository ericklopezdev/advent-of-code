file_path = '11.txt'

def main():
    try:
        with open(file_path, 'r') as file:
            lines = file.read().strip().splitlines()
        graph = {}
        for line in lines:
            parts = line.split(': ')
            dev = parts[0]
            outs = parts[1].split()
            graph[dev] = outs
        memo = {}
        def count_paths(node):
            if node == "out":
                return 1
            if node in memo:
                return memo[node]
            res = 0
            for nei in graph.get(node, []):
                res += count_paths(nei)
            memo[node] = res
            return res
        print(count_paths("you"))
    except FileNotFoundError:
        print(f"[error]: file {file_path} not found")

main()
