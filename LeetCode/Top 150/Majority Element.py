from collections import Counter


def majorityElement(nums) -> int:
    # hashmap = {}
    # count = len(nums) // 2
    
    # for v in nums:
    #     hashmap[v] = hashmap.get(v, 0) + 1
    #     if hashmap.get(v) > count:
    #         return v

    hashmap = dict(Counter(nums))
    mx = len(nums)/2
    for item in hashmap.items():
        key, val = item
        if val > mx:
            return key



if __name__ == "__main__":
    inpt = [2,2,1,1,1,2,2]
    result = majorityElement(inpt)
    print(result)