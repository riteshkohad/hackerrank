
def find_all_subsets(nums):
    n = len(nums)
    result, temp = [], []

    def search(i):
        if i == n:
            result.append(temp.copy())
            return
        
        # dont pick i
        search(i + 1)

        # pick i 
        temp.append(nums[i])
        search(i + 1)
        temp.pop()
    
    search(0)
    return result


# def find_all_subsets2(nums):
#     n = len(nums)
#     result = []

#     def search(i):
#         if i == n:
#             result = result.copy()
#             return
        
#         # dont pick i
#         search(i + 1)

#         # pick i 
#         result.append(nums[i])
#         search(i + 1)
#         result.pop()
    
#     search(0)
#     return result


if __name__ == "__main__":
    inpt = [3, 6, 9]
    result = find_all_subsets(inpt)
    print(result)