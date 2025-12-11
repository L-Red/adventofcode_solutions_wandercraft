from collections import deque

def convolution2d(array):
    filter = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    sum = 0;
    m = len(array)
    n = len(array[0])
    new_array = [[0 for _ in range(n+2)] for _ in range(m+2)]
    ret_array = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            new_array[i][j] = array[i-1][j-1]

    for i in range(1, m+1):
        for j in range(1, n+1):
            if new_array[i][j] == 0:
                continue
            temp_sum = 0
            for k in range(3):
                for l in range(3):
                    temp_sum += new_array[i+k-1][j+l-1] * filter[k][l]
            ret_array[i-1][j-1] = temp_sum  
    return ret_array

def print_2d_array(array):
    for line in array:
        print(line)

def solve(forklifts, summed):
    
    m = len(forklifts)
    n = len(forklifts[0])

    final_sum = 0

    queue = deque()
    for i in range(m):
        for j in range(n):
            if forklifts[i][j] == 1 and summed[i][j] < 4:
                queue.append((i, j))

    neighbours = [(0,1), (0,-1), (1,0), (-1,0), (1,1), (1,-1), (-1,1), (-1,-1)]

    while queue:
        i, j = queue.popleft()

        if forklifts[i][j] == 0:
            continue

        if summed[i][j] >= 4:
            continue

        final_sum += 1
        forklifts[i][j] = 0

        for di, dj in neighbours:
            ni, nj = i + di, j + dj
            if 0 <= ni < m and 0 <= nj < n and forklifts[ni][nj] == 1:
                summed[ni][nj] -= 1
                if summed[ni][nj] < 4:
                    queue.append((ni, nj))

    return final_sum
    
    

if __name__ == '__main__':

    # get input
    input = []
    with open('inputs/day4_input.txt', 'r') as file:
        for line in file:
            input.append(line.strip())



    forklifts = [list(map(lambda x: 1 if x == '@' else 0, l)) for l in input]

    summed = convolution2d(forklifts)
    
    print(solve(forklifts, summed))
