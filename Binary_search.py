

def binary_search(this_array, this_value, start, end) -> int :
    mid_pos = int((start + end) / 2)
    mid_val = this_array[mid_pos]

    if mid_val == this_value:
        return mid_pos
    elif start == end:
        return -1
    elif mid_val > this_value:
        end = mid_pos - 1
        return binary_search(this_array, this_value, start, end)
    elif mid_val < this_value:
        start = mid_pos + 1
        return binary_search(this_array, this_value, start, end)


if __name__ == "__main__":

    arr = [2,7, 9, 11, 20, 25, 27, 50, 51, 60]
    val_to_find = 25
    start = 0
    end = len(arr) - 1

    print(binary_search(arr, val_to_find, start, end))
