'''
Input: a List of integers
Returns: a List of integers
'''
from itertools import repeat 

def moving_zeroes(arr):
    zeros = arr.count(0)            # find how many 0s are in the arr
    for i in range(len(arr)):       # loop through the whole array
        if 0 in arr:                # delete all the 0s
            arr.remove(0)
    
    arr.extend(repeat(0, zeros))    # add the same number of 0s from the begining to the end
    
    return arr

if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")