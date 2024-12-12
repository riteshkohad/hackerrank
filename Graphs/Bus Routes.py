
def minimum_buses(bus_routes, src, dest):
    if src == dest:
        return 0
        
    adj_list = {}
    bus = 0
    for bus_route in bus_routes:
        bus += 1
        for i in range(len(bus_route)):
            s = bus_route[i]
            nxt = i + 1 if i < len(bus_route)-1 else 0
            s1 = bus_route[nxt]
            if s in adj_list:
                adj_list[s].append((s1, bus))
            else:
                adj_list[s] = [(s1, bus)]

    print(adj_list)

    stack = [src]
    visited = set()
    bus_count = 0
    visited.add(src)
    last_bus = -1
    while stack:
        start = stack.pop()
        if start not in adj_list:
            return -1

        stations = adj_list[start]

        for station, bus in stations:
            if station in visited:
                continue 

            if last_bus == -1:
                last_bus = bus
                bus_count = 1
            else:
                if last_bus != bus:
                    last_bus = bus
                    bus_count += 1
            
            if station == dest:
                return bus_count
            else:
                stack.append(station)
                visited.add(station)
            

    # Replace this placeholder return statement with your code
    return -1


if __name__ == "__main__":
    inpt = [[1,12],[10,5,9],[4,19],[10,12,13]]
    inpt2 = 1
    inpt3 = 9
    result = minimum_buses(inpt, inpt2, inpt3)
    print(result)
