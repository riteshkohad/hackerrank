

def search(arr, target):
    s, e = 0, len(arr) -1

    while s <= e:
        mid = (s + e) // 2

        print(f"mid: {mid} val: {arr[mid]}")

        if arr[mid] == target:
            return True
        
        if arr[s] < arr[mid]:
            if arr[s] <= target < arr[mid]:
                e = mid - 1
            else:
                s = mid + 1
        elif arr[s] > arr[mid]:
            if arr[mid] < target <= arr[e]:
                s = mid + 1
            else:
                e = mid - 1
        else:
            s += 1

    return False
    

if __name__ == "__main__":
    inpt = [1,3,1,1,1]
    t = 3
    result = search(inpt, t)
    print(result)
