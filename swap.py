

def find_swap(len, arr):
    swap_count = 0

    for i in range(1, len+1):
        diff = i - arr[i-1]
        if diff < 0:
            if diff < -2:
                print("too Chaotic")
                return
            else:
                swap_count += abs(diff)

    print(swap_count)

if __name__ == "__main__":
    print("I am here")

    this_array = [2, 1, 5, 3, 4]
    this_len = len(this_array)

    find_swap(this_len, this_array)
