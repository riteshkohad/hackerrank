

def rescue_boats(people, limit):
    people.sort()
    left, right = 0, len(people) - 1

    boats = 0
    while left <= right:
        if people[left] + people[right] <= limit:
            left += 1
            right -= 1
        else:
            right -= 1

        boats += 1

    return boats


if __name__ == "__main__":
    inpt = [3,1,4,2,4]
    lmt = 4
    result = rescue_boats(inpt, lmt)
    print(result)