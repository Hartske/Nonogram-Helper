def find_remainder(length, lst):
    total = 0
    for i in range(len(lst) - 1):
        total += lst[i] + 1
    total += lst[(len(lst) - 1)]
    remainder = length - total
    return remainder

def check_overlap(lst, remainder):
    for e in lst:
        if e > remainder:
            return 'True'
    return 'False'

def mark(sqrs, lst, remainder):
    index = 0
    for e in lst:
        if e > remainder:
            index += remainder
            for s in sqrs[index:(index - remainder + e)]:
                s.is_marked = True
                index += 1
            index += 1
        else:
            index += e + 1
    return sqrs
