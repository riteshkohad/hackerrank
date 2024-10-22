

def candy(ratings) -> int:
    candies = [1] * (len(ratings))
    # print(candies)

    for i in range(1, len(ratings)):
        if ratings[i] > ratings[i - 1]:
            candies[i] = candies[i - 1] + 1
    
    # print(candies)

    for i in range(len(ratings) -2, -1, -1):
        if ratings[i] > ratings[i + 1]:
            candies[i] = max(candies[i], candies[i + 1] + 1)

    # print(candies)

    return sum(candies)

if __name__ == "__main__":
    inpt = [1,2,2]
    result = candy(inpt)
    print(result)