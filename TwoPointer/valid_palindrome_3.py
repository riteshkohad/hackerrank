def is_valid_palindrome(this_str):
    s, e = 0, len(this_str) - 1
    # print(f"start is {s} and end is {e}")
    while s < e:
        # print(f"s: {this_str[s]} and e: {this_str[e]}")
        if this_str[s] != this_str[e]:
            # print("String is not palindrome")
            return False

        s += 1
        e -= 1

    # print("String is palindrome")
    return True


if __name__ == "__main__":
    print(is_valid_palindrome("RACECAR"))