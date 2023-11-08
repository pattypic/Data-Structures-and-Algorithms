#  File: Work.py
#  Name: Patrick Pichardo

import sys , time

# Purpose: Determines how many lines of code will be written before the coder crashes to sleep. Must be implemented using recursion.
# Input: lines_before_coffee - how many lines of code to write before coffee / prod_loss - factor for loss of productivity after coffee
# Output: returns the number of lines of code that will be written before the coder falls asleep

def sum_series(lines_before_coffee, prod_loss,num_coffee = 0):  # implemented using recursion, initally done with a while loop.
    num_lines = lines_before_coffee // prod_loss ** num_coffee  # math. added the num_coffee = 0 for simplicity 
    if num_lines < 1:       # checks how many lines the coder is writing, if it is less than 1
        return 0            # break point aka when coder falls asleep
    else:                   
        return num_lines + sum_series(lines_before_coffee, prod_loss, num_coffee + 1)   # recursively finds how many lines the coder can make after each coffee

# Purpose: Uses a linear search to find the initial lines of code to write before the first cup of coffee, so that the coder will complete the total lines of code before sleeping AND get to have coffee as soon as possible.
# Input: total_lines - lines of code that need to be written / prod_loss - factor for loss of productivity after each coffee
# Output: returns the initial lines of code to write before coffee

def linear_search(total_lines, prod_loss):
    initial_lines = 0  # creates inital lines of code
    total_for_initial_lines = 0 # count variable
    for _ in range(total_lines):    # empty loop, prefer for loops for linear searches. 
        total_for_initial_lines += 1    # increment count
        initial_lines += 1          # increment inital lines 
        num_lines = sum_series(initial_lines, prod_loss)  # checks for num of lines for given instance
        if num_lines >= total_lines:            # check of said instance == to total_lines, i dont think i need the >= but i submitted the code already and i dont want to change it
            return initial_lines,total_for_initial_lines
    return initial_lines,total_for_initial_lines
  
# Purpose: Uses a binary search to find the initial lines of code to write before the first cup of coffee, so that the coder will complete the total lines of code before sleeping AND get to have coffee as soon as possible.
# Input: total_lines - lines of code that need to be written / prod_loss - factor for loss of productivity after each coffee
# Output: returns the initial lines of code to write before coffee

def binary_search(total_lines, prod_loss):
    lo,hi=1,total_lines     # creating high and low for B search, set high to value of total lines
    initial_lines = 0       # Creating inital lines
    total_for_initial_lines = 0 # using the same count method as lin search
    
    while lo <= hi:         # creating loop break out if result is not between low and high, it will be tho.
        mid = (lo + hi) // 2    # find mid
        num_lines = sum_series(mid, prod_loss)  # how many lines the mid num can make
        total_for_initial_lines += 1    # increment the count
        if num_lines == total_lines:    # True condition, if the mid num lines == to total lines
            initial_lines = mid         # sets init lines to mid to return it
            break                       # break loop
        elif num_lines > total_lines:   # False condition, if mid num lines greater than tot, set hi to mid -1 so we dont repeat mid 
            initial_lines = mid         # and in the case result doesnt exist we can break the while loop
            hi = mid - 1
        else:                           # False conditions left. 
            lo = mid + 1
    return initial_lines, total_for_initial_lines

''' ##### DRIVER CODE #####
    ##### Do not change, except for the debug flag '''

def main():

    # Open input source
    # Change debug to false before submitting
    debug = True
    if debug:
        in_data = open('work.in')
    else:
        in_data = sys.stdin

    # read number of cases
    line = in_data.readline().strip()
    num_cases = int(line)

    for i in range(num_cases):

        # read one line for one case
        line = in_data.readline().strip()
        data = line.split()
        total_lines = int(data[0])  # total number of lines of code
        prod_loss = int(data[1])  # read productivity loss factor

        print("=====> Case #", i + 1)

        # Binary Search
        start = time.time()
        print("Binary Search:")
        lines, count = binary_search(total_lines, prod_loss)
        print("Ideal lines of code before coffee:", lines)
        print("sum_series called", count, "times")
        finish = time.time()
        binary_time = finish - start
        print("Elapsed Time:", "{0:.8f}".format(binary_time),
              "seconds")
        print()

        # Linear Search
        start = time.time()
        print("Linear Search:")
        lines, count = linear_search(total_lines, prod_loss)
        print("Ideal lines of code before coffee:", lines)
        print("sum_series called", count, "times")
        finish = time.time()
        linear_time = finish - start
        print("Elapsed Time:", "{0:.8f}".format(linear_time),
              "seconds")
        print()

        # Comparison
        print("Binary Search was",
              "{0:.1f}".format(linear_time / binary_time),
              "times faster.")
        print()
        print()


if __name__ == "__main__":
    main()
