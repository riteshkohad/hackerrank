

def canCompleteCircuit(gas, cost) -> int:
    if sum(gas) < sum(cost):
        return -1

    total = result = 0

    for i in range(len(gas)):
        total += (gas[i] - cost[i])
        print(total)

        if total < 0:
            total = 0
            result = i + 1
    
    return result

    


if __name__ == "__main__":
    inpt1 = [1,2,3,4,5]
    inpt2 = [3,4,5,1,2]

    result = canCompleteCircuit(inpt1, inpt2)
    print(result)
