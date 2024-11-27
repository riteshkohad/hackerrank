
def network_delay_time(times, n, k):
    adj_list = {i + 1 :[] for i in range(n)}
    for src, tar, time in times:
        adj_list[src].append((tar, time))
    print(adj_list)
    visited = set()
    stack = []
    stack.append(adj_list[k])
    visited.add(k)
    max_dist = 0

    while stack:
        item = stack.pop()
        total_dis = 0
        if item:
            for node, dist in item:
                print(f"node: {node} dist: {dist}")
                max_dist = max(max_dist, dist)
                if node not in visited:
                    stack.append(adj_list[node])
                    visited.add(node)
            
    return max_dist


if __name__ == "__main__":
    inpt = [[1,2,1],[2,3,1],[3,4,1]]
    inpt2 = 4
    inpt3 = 1
    result = network_delay_time(inpt, inpt2, inpt3)

    print(result)