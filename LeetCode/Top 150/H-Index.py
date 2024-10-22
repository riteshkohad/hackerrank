
# Solution 1
def hIndex(citations) -> int:
    if not citations:
        return 0

    freq = [0] * (len(citations) + 1)
    ln = len(citations) 

    for i, val in enumerate(citations):
        idx = val if val < ln else ln
        freq[idx] += 1

    cita = 0
    for i in range(len(freq) -1, -1, -1):
        cita += freq[i]
        if cita >= i:
            return i 

    return 0

# solution 2
def hIndex_ii(citations):
    ln = len(citations)
    citations.sort()

    for i, val in enumerate(citations):
        if val >= (ln - i):
            return (ln - i)
    
    return 0 

if __name__ == "__main__":
    inpt = [3,0,6,1,5]
    result = hIndex(inpt)
    print(result)

    result = hIndex_ii(inpt)
    print(result)
