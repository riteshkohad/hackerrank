import heapq


def k_closest(points, k):
    # declare a min heap
    min_heap = []

    # push all the values as tuple in it
    for i in range(len(points)):
        val = (points[i][0] * points[i][0])  + (points[i][1] * points[i][1])
        tpl = (val, points[i])
        heapq.heappush(min_heap, tpl)

    # define result array
    result = []
    # pop min k values from heap
    for i in range(k):
        tpl = heapq.heappop(min_heap)
        result.append(tpl[1])

    # return 
    return result


if __name__ == "__main__":
    inpt = [[-1,-3],[-4,-5],[-2,-2],[-2,-3]]
    k = 3
    result = k_closest(inpt, k)
    print(result)