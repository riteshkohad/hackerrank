"""
Time complexity:
The time complexity of the function sum_of_squared_digits is O(log n), where n is the input number. 
This is because the number of iterations in the while loop is proportional to the number of digits in the input number, which is log n.

The time complexity of the function is_happy_number is O(log n), where n is the input number. 
This is because the while loop in the function runs until the fast pointer reaches 1 or the fast and slow pointers meet. 
In the worst case, the fast pointer can reach a cycle of repeating numbers, which is bounded by the number of digits in the 
input number, which is log n. Therefore, the overall time complexity is O(log n).

Space complexity:
The space complexity of the function Happy Number is O(1) because it only uses a constant amount of space to store the variables 
slow, fast, and total_sum. The space complexity of the built-in Python functions invoked by the code, such as modulus operator (%), 
integer division operator (//), and exponentiation operator (**), is also O(1) because they do not require any additional space.

"""



# Helper function to calculate sum of squared digits 
def sum_of_squared_digits(number): 
    # variable to keep track of sum
    total_sum = 0

    # loop to keep calculating sum
    while number > 0:
        # take a one digit 
        digit = number % 10

        # take divisor 
        number = number // 10

        # update sum of taken digit's square 
        total_sum += digit ** 2

    # return total sum 
    return total_sum


# function to check if number is happy 
def is_happy_number(n):
    # define fast and slow pointers 
    slow = n
    fast = sum_of_squared_digits(n)
    
    # loop thru till cycle repeats or finds a happy number 
    while fast != 1 and fast != slow:
        # increment slow pointer by one iteration 
        slow = sum_of_squared_digits(slow)

        # increment fast pointer by two iterations 
        fast = sum_of_squared_digits(sum_of_squared_digits(fast))
    
    # check if happy number found
    if fast == 1:
        return True
    else:
        return False




if __name__ == "__main__":
    inp_num = 7
    result = is_happy_number(inp_num)
    print(result)