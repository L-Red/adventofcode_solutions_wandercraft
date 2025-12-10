def aux(bank, left, right):
    if left == right: # leaf case, return just the digits
        return 0, int(bank[left])
    else: # node case, combine max digits and check max
        mid = (left + right) // 2
        maxLeft, maxDigitLeft = aux(bank, left, mid)
        maxRight, maxDigitRight = aux(bank, mid + 1, right)
        return max(max(maxLeft, maxRight), maxDigitLeft*10 + maxDigitRight), max(maxDigitLeft, maxDigitRight)

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
        maxi, maxDigit = aux(bank, 0, len(bank)-1)
        sum += maxi
    print(sum)