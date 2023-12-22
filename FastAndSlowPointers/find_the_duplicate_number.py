
def find_duplicate(nums):
    slow = 0
    fast = 0
    for i in range(len(nums)):
        slow = slow + 1
        fast = fast + 2

        if slow == fast:
            slow = 0 

            for j in range(len(nums)):
                slow = slow + 1 
                fast = fast + 1

                if slow == fast:
                    return fast

    # Replace this placeholder return statement with your code
    
    return 0

if __name__ == "__main__":
    inpt = [1,3,4,2,2]

    ret_val = find_duplicate(inpt)
    print(ret_val)