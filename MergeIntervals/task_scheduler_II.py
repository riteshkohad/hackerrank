
def least_time(tasks, n):
    frequencies = {}

    for t in tasks:
        frequencies[t] = frequencies.get(t,0) + 1

    frequencies = dict(sorted(frequencies.items(), key=lambda x:x[1]))
    print(f"Frequencies sorted: {frequencies}")

    max_item = frequencies.popitem()
    max_freq = max_item[1]
    idle_time = (max_freq -1) * n

    print(f"Max freq: {max_freq} max idle time: {idle_time}")
    
    while frequencies and idle_time > 0:
        curr_item = frequencies.popitem()
        idle_time -= min(max_freq - 1, curr_item[1] )
    
    idle_time = max(0, idle_time)

    return len(tasks) + idle_time



if __name__ == "__main__":
    inpt = ['C', 'A', 'B', 'C', 'A', 'A', 'D', 'B', 'C']
    inpt2= 3

    result = least_time(inpt, inpt2)
    print(result)

