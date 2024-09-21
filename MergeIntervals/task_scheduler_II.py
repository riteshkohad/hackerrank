
def least_time(tasks, n):
    # declare the hashmap 
    frequencies = {}

    # load hashmap with all the tasks and its frequencies 
    for t in tasks:
        # check existing task in the hashmap and add 1 to it
        # if task does not exist, 2nd argument of get will be returned as a default value 
        frequencies[t] = frequencies.get(t,0) + 1

    # sort the hashmap based on the frequencies of each task 
    # remember sort ascending 
    frequencies = dict(sorted(frequencies.items(), key=lambda x:x[1]))
    
    # once sorted, hashmap will return last value with popitem(), it will return tuple ("A", 3)
    max_item = frequencies.popitem()
    # take a frequency of a task 
    max_freq = max_item[1]
    # calculate the maximum idle time needed to make it work 
    idle_time = (max_freq -1) * n

    # loop thru the remaining tasks in the hashmap and try to fit in the max time
    while frequencies and idle_time > 0:
        # take next item 
        curr_item = frequencies.popitem()
        # fit it in the existing idle time, (Remember, while idle, CPU can run other task)
        idle_time -= min(max_freq - 1, curr_item[1] )
    
    # if it is -ve, make it zero otherwise take remaining idle time
    idle_time = max(0, idle_time)

    # return the length of task + remaining idle time
    return len(tasks) + idle_time



if __name__ == "__main__":
    inpt = ['C', 'A', 'B', 'C', 'A', 'A', 'D', 'B', 'C']
    inpt2= 3

    result = least_time(inpt, inpt2)
    print(result)

