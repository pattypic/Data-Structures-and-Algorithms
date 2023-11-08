#  File: Spiral.py
#  Name: Patrick Pichardo

import sys

# Input: n
# Output:
def get_dimension(in_data): 
    x = int(in_data.readline().strip())  
    return x

# Input: n is an odd integer between 1 and 100
# Output: returns a 2-D list representing a spiral
#         if n is even add one to n
def create_spiral(n):
    if n % 2 == 0:
        n += 1

    spiral = [[0 for _ in range(n)] for _ in range(n)]
    x,y = 0,n-1
    spiral[x][y] = n * n
    
    while spiral[x][y] != 1:
        while y > 0 and spiral[x][y-1] == 0:
            y -= 1
            spiral[x][y] = spiral[x][y+1] - 1
        while x < n - 1 and spiral[x+1][y] == 0:
            x += 1
            spiral[x][y] = spiral[x-1][y] - 1
        while y < n - 1 and spiral[x][y+1] == 0:
            y += 1
            spiral[x][y] = spiral[x][y-1] - 1
        while x > 0 and spiral[x-1][y] == 0:
            x -= 1
            spiral[x][y] = spiral[x+1][y] - 1
    return spiral

# Input: handle to input file
#        the number spiral
# Output: printed adjacent sums
def print_adjacent_sums(in_data, spiral):
    adjacent_sums = []
    data = in_data.readlines()
    for i in data:
        i = i.strip()
        if i == data[0]:
            continue 
        try:
            sums = sum_adjacent_numbers(spiral, int(i))
            if sums is None:
                print(0)
                adjacent_sums.append(0)
            else:
                print(sums)
                adjacent_sums.append(sums)
        except (ValueError,TypeError):
            print("Invalid data")
            adjacent_sums.append("Invalid data")
    return adjacent_sums

# Input: the number spiral
#        the number to find the adjacent sum for
# Output: integer that is the sum of the
#         numbers adjacent to n in the spiral
#         if n is outside the range return 0
def sum_adjacent_numbers(spiral, n):
    x, y = len(spiral), len(spiral[0])
    sums = 0
    for x_i, x_v in enumerate(spiral):
        if n in x_v:
            y_i = x_v.index(n) # finds n index
            for i in range(-1, 2):
                for j in range(-1, 2):
                    new_x, new_y = x_i + i, y_i + j
                    # the first two snipbits of code makes we are within spiral. 
                    # the last excludes the center point
                    if 0 <= new_x < x and 0 <= new_y < y and (i != 0 or j != 0):
                        sums += spiral[new_x][new_y] # All works
            return sums 
    return None # handles if n doesnt exist

# Added for debugging only. No changes needed.

def print_spiral(spiral):
    for i in range(0, len(spiral)):
        for j in range(0, len(spiral[0])):
            row_format = '{:>4}'
            print(row_format.format(spiral[i][j]), end='')
        print()

def main():

    debug = False
    if debug:
        in_data = open('spiral.in')
    else:
        in_data = sys.stdin

    size = get_dimension(in_data)       # process the lines of input

    # create the spiral
    spiral = [[]]
    spiral = create_spiral(size)
    # use following line for debugging only
    # print_spiral(spiral)

    print_adjacent_sums(in_data, spiral)        # process adjacent sums


if __name__ == "__main__":
    main()