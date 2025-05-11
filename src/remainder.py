def find_remainder(length, lst):
    total = 0
    print(f'lst: {lst}')
    for i in range(len(lst) - 1):
        total += lst[i] + 1
    total += lst[(len(lst) - 1)]
    remainder = length - total
    print(f'Remainder: {remainder}')
    return remainder

def convert_list(lst):
    no_space = lst.replace(" ", "")
    converted = no_space.split(",")
    for e in converted:
        int(e)
    return converted