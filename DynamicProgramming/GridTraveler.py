# using recurrestion 
def grid_traveler(row, col):
    if row == 1 and col == 1:
        return 1
    
    if row == 0  or col == 0:
        return 0

    return grid_traveler(row -1, col) + grid_traveler(row, col-1)

# using dynamic programming 
def grid_traveler_dp(row, col, cache={}):
    key = str(row) + "," + str(col)

    if key in cache:
        return cache[key]

    if row == 1 and col == 1:
        return 1
    
    if row == 0  or col == 0:
        return 0

    res = grid_traveler_dp(row -1, col, cache) + grid_traveler_dp(row, col-1, cache)
    cache[key] = res
    return res


if __name__ == "__main__":
    print(grid_traveler(2,2))
    print(grid_traveler_dp(20,20))