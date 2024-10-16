
def find_closest_elements(nums, k, target):
    dist = []

    for i in nums:
        tpl = (i - target, i)
        dist.append(tpl)


    return dist


if __name__ == "__main__":
    inpt = [1,2,3,4,5]
    k = 4
    t = 3
    result = find_closest_elements(inpt, k, t)
    print(result)