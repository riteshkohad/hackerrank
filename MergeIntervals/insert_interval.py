

def insert_interval(existing_intervals, new_interval):
    output = []
    i=0

    while i < len(existing_intervals) and existing_intervals[i][0] < new_interval[0]:
        output.append(existing_intervals[i])
        i += 1
    
    lst_item = output[-1]

    if lst_item[1] <= new_interval[0]:
        output.append(new_interval)
    else:
        # output[-1][0] = min(lst_item[0], new_interval[0])
        output[-1][1] = max(lst_item[1], new_interval[1])

    while i < len(existing_intervals):
        start, end = existing_intervals[i][0], existing_intervals[i][1]
        lst = output[-1]
        lst_end = lst[1]

        if end <= lst[0]:
            output.append([start, end])
        else:
            # output[-1][0] = min(output[-1][0], start)
            output[-1][1] = max(output[-1][1], end)
        
        i += 1


        # if end <= new_interval[0] or start <= new_interval[1]:
        #     new_st = min(start, new_interval[0])
        #     new_ed = max(end, new_interval[1])

        #     if new_st <= lst_end:
        #         output[-1][0] = min(new_st, lst[0])
        #         output[-1][1] = max(new_ed, lst[1])
        #     else:
        #         output.append([new_st, new_ed])
        # else:
        #     output.append([start,end])


    return output


def main():
    inpt = [[1,2],[3,4],[5,8],[9,15]]
    new_int = [2,5]

    ret_val = insert_interval(inpt, new_int)
    print(ret_val)



if __name__ == "__main__":
    main()