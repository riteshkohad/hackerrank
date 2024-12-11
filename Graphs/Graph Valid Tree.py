

def valid_tree(n, edges):
    if len(edges) != n-1:
        return False
        
    adj_list = {i: [] for i in range(n)}
    for n1, n2 in edges:
        adj_list[n1].append(n2)
        adj_list[n2].append(n1)

    visited = set()
    stack = [0]
    visited.add(0)

    while stack:
        item = stack.pop()
        
        for neg in adj_list[item]:
            if neg not in visited:
                visited.add(neg)
                stack.append(neg)

    return len(visited) == n

if __name__ == "__main__":
    inpt = 5
    inpt2 = [[0,1],[0,2],[0,3],[3,4]]
    result = valid_tree(inpt, inpt2)
    print(result)