

def intervals_intersection(interval_list_a, interval_list_b):
    i , j = 0 , 0
    output = []

    while i < len(interval_list_a) and j < len(interval_list_b):
        a_start, a_end = interval_list_a[i][0], interval_list_a[i][1]
        b_start, b_end = interval_list_b[j][0], interval_list_b[j][1]
        int_start, int_end = 0, 0

        if a_start <= b_end and b_start <= a_end:
            int_start = max(a_start, b_start)
            int_end = min(a_end, b_end)
            output.append([int_start, int_end])   
        
        if a_end < b_end:
            i += 1
        elif a_end > b_end:
            j += 1
        else:
            i += 1
            j += 1

    return output



if __name__ == "__main__":
    inpt1 = [[1,4],[5,6],[7,8],[9,15]]
    inpt2 = [[2,4],[5,7],[9,15]]
    result = intervals_intersection(inpt1, inpt2)
    print(result)