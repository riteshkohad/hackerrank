
# NOTE: this is fast and slow pointer but in leetcode it is considered as two pointers 


def sum_digits(num: int):
    total = 0
    for s in str(num):
        total += (int(s) * int(s))
    
    return total


def isHappy(n: int) -> bool:
    sum_one = sum_digits(n)
    sum_two = sum_digits(sum_digits(n))
    
    while sum_one != 1:
        sum_one = sum_digits(sum_one)
        sum_two = sum_digits(sum_digits(sum_two))
        # print(f"one:{sum_one} | two: {sum_two}")

        if sum_one == sum_two and sum_one != 1:
            # print(f"one:{sum_one} | two: {sum_two}")
            return False
    
    return True



def main():
    inpt = 7
    ret_val = isHappy(inpt)
    print(ret_val)

if __name__ == "__main__":
    main()