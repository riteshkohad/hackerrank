

def first_bad_version(n):
    s, e = 1, n
    api_calls = 0

    while s < e:
        m = (s + e) // 2
        api_calls += 1
        if is_bad_version(m):
            e = m
        else:
            s = m + 1

    return [s, api_calls]


if __name__ == "__main__":
    inpt = 5
    result = first_bad_version(inpt)
    print(result)