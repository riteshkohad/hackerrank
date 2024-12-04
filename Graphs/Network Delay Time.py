
# this code needs to be updated with priority queue or min heap instead of stack 
def network_delay_time(times, n, k):
    adj_list = {i + 1 :[] for i in range(n)}
    for src, tar, time in times:
        adj_list[src].append((tar, time))
    # print(adj_list)
    visited = set()
    stack = []
    stack.append((k, 0))
    visited.add(k)
    max_dist = 0

    while stack:
        nd, dt = stack.pop()
        if nd is visited:
            continue

        visited.add(nd)
        
        for node, dist in adj_list[nd]:
            # print(f"node: {node} dist: {dist}")
            if node in visited:
                continue

            time = dt + dist
            max_dist = max(max_dist, time)
            # print(f"nd: {nd} dt: {dt} | Node: {node} dist: {dist} max: {max_dist}")
            stack.append((node, time))

    if len(visited) == n:
        return max_dist                
            
    return -1


if __name__ == "__main__":
    inpt = [[2, 1, 1], [3, 2, 1], [3, 4, 2]]
    inpt2 = 4
    inpt3 = 3
    result = network_delay_time(inpt, inpt2, inpt3)

    print(result)