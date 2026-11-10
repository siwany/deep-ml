def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
    if len(a[0]) != len(b[0]):
        return -1
    final = []
    b_t = list(zip(*b))
    for a_list in a:
        result = []
        for b_list in b_t:
            result.append(sum(x * y for x, y in zip(a_list, b_list)))
        final.append(result)
    return final