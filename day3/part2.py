def maxIndex(bank, idx1, idx2):
    if int(bank[idx1]) > int(bank[idx2]):
        return idx1
    else:
        return idx2

def aux(bank, left, right):
    dct = {}
    for (idx, digit) in enumerate(bank):
        new_dct = {}
        for i in range(idx +1):
            if i == 0:
                if 1 not in dct:
                    new_dct[1] = int(digit)
                elif int(digit) > dct[1]:
                    new_dct[1] = int(digit)
                else:
                    new_dct[1] = dct[1]
            elif i+1 not in dct:
                new_dct[i+1] = dct[i]*10 + int(digit)
            else:
                new_dct[i+1] = max(dct[i+1], dct[i]*10 + int(digit))
        dct = new_dct
        # print("longet at length: ", idx+1, "is: ", dct[idx+1])
    return dct[12]

if __name__ == '__main__':

    # get input
    input = []
    with open('inputs/day3_input.txt', 'r') as file:
        for line in file:
            input.append(line.strip())

    # set sum
    sum = 0

    # add up the invalid ids
    for bank in input:
        maxi = aux(bank, 0, len(bank)-1)
        # print("bank: ", bank, "joltage: ", maxi)
        sum += maxi
    print(sum)