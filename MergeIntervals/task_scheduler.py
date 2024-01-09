

# Incomplete solution 

def least_time(tasks, n):
    mp = {}

    for i in tasks:
        if i in mp:
            mp[i] = mp[i] + 1
        else:
            mp[i] = 1

    mp = dict(sorted(mp.items(), key=lambda x:x[1]))
    print(mp)
    print(mp.popitem())
    print(mp)
    
    return "hello 1"


def main():
    inpt = ["A","A","B","B","B", "C"]
    num = 2 
    ret_val = least_time(inpt, num)
    print(ret_val)


if __name__ == "__main__":
    main()