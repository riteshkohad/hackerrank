

def sum_of_sq_digits(num):
    sum_of_digits = 0
    while num > 0:
        digit = num % 10
        num = num // 10

        sum_of_digits += digit ** 2

    return sum_of_digits


def is_happy_number(n):
    slow, fast = n, sum_of_sq_digits(n)
    
    while fast != 1 and fast != slow:
        slow = sum_of_sq_digits(slow)
        fast = sum_of_sq_digits(sum_of_sq_digits(fast))
    
    if fast == 1:
        return True
    else:
        return False




if __name__ == "__main__":
    digit = 4
    print(sum_of_sq_digits(digit))
    print(is_happy_number(digit))