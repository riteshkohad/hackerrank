"""
Solution summary
1. To recap, the solution to this problem can be divided into five main parts:
2. We traverse the array using three pointers, red, white, and blue.
3. If the element pointed to by the white pointer is 0, we swap it with the element pointed to by the red pointer if it’s not pointing to 
    0, and increment both the red and white pointers.
4. If the element pointed to by the white pointer is 1, we increment the white pointer.
5. If the element pointed to by the white pointer is 2, we swap it with the element pointed to by the blue pointer if it’s not pointing to 
    2 and decrement the blue pointer.
6. The array is sorted when the blue pointer becomes less than the white pointer.

Time complexity
The time complexity of this solution is O(n) since we’re only traversing the array once.

Space complexity
The space complexity of this solution is O(1) since no extra space is used.  
"""


def sort_colors(colors):
    # declare red and white pointer with the beginning of the list
    red = white = 0

    # declare blue pointer with the end of the list as it should be at the end
    blue = len(colors)-1

    # iterate thru the length of the array 
    for x in range(len(colors)):
        # check color at the white index (because white should be in the middle after sorting)
        if colors[white] == 0:
            # if it is 0 which is red, then swap with color[red] 
            tmp = colors[white]
            colors[white] = colors[red]
            colors[red] = tmp

            # move the pointers 
            white += 1
            red += 1

        elif colors[white] == 1:
            # if color[white] is 1 which is white, then it is at the right place
            # don't swap, just increment the white index 
            white += 1
        else :
            # otherwise (color[white] == 2 which is for blue) 
            # swap color[white] with blue and decrement blue index value by 1 as 
            # 2 is properly secured at the end of the list
            tmp = colors[white]
            colors[white] = colors[blue]
            colors[blue] = tmp

            blue -= 1

    # return the sorted list
    return colors


if __name__ == "__main__":
    inputList = [0,1,0]
    sortedList = sort_colors(inputList)
    print(sortedList)