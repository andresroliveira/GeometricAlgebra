def diagonal_entry(id):
    return 1

def metric_factor(mask):
    index = 0
    result = 1
    while mask != 0:
        if (mask & 1) != 0:
            result *= diagonal_entry(index)
        mask >>= 1
        index += 1
    return result

def signature(n: int):
    s = [canonical_reorder(i) for i in range(1<<n)]

def outer_product(coef1, mask1, coef2, mask2):
    if mask1 & mask2 == 0:
        sign = canonical_reorder(mask1, mask2)
        coef = sign * coef1 * coef2
        mask = mask1 | mask2
        return coef, mask

    return 0, 0

def geometric_product(coef1, mask1, coef2, mask2):
    # print(coef1, bin(mask1,3), coef2, bin(mask2, 3))
    sgn = canonical_reorder(mask1, mask2)
    metric = metric_factor(mask1 & mask2)
    coef = sgn * metric * coef1 * coef2
    mask = mask1 ^ mask2

    # if coef != 0:
    #     print('dor', bin(mask,3), coef)
    #     print(coef1, mask1, coef2, mask2)
    return coef, mask

def colision(mask):
    return mask.bit_count()

bin = lambda x, n: format(x, 'b').zfill(n)

def canonical_reorder(mask1: int, mask2: int):
    # print(bin(mask1, 4), bin(mask2, 4))

    swap = 0

    mask1 = mask1 >> 1

    while mask1 != 0:
        # print(bin(mask1, 4), bin(mask2, 4))
        swap += colision(mask1 & mask2)
        mask1 = mask1 >> 1


    if swap & 1 == 0:
        return 1
    
    return -1

if __name__ == '__main__':
    # print(canonical_reorder(1<<1 | 1 << 2 , 1 << 0 | 1 << 4 - 1))

    for i in range(1 << 3):
        print(metric_factor(i))
