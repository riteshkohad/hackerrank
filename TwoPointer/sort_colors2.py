def sort_colors(colors):
    red, current, blue = (0,0, len(colors) -1 )

    while current <= blue:
        if colors[current] == 0:
            tmp = colors[red]
            colors[red] = colors[current]
            colors[current] = tmp
            red += 1
            current += 1
        elif colors[current] == 1:
            current += 1
        else:
            tmp = colors[blue]
            colors[blue] = colors[current]
            colors[current] = tmp
            blue -=1
    
    return colors


if __name__ == "__main__":
    ary = [2,1,1,0,0]
    clrs = sort_colors(ary)
    print(clrs)


