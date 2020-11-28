def ReturnSurvivor(n, k):
    p = 0
    p_list = [];
    while p < n:
        p_list.append(p)
        p += 1

    i = 0
    j = 0
    while len(p_list) > 1:
        if i > len(p_list) - 1:
            i = 0
        j += 1
        if j != k:
            pass
        else:
            del (p_list[p])
            j = 0
            i -= 1
        i += 1
    return p_list[0]
