'''
Input: a List of integers
Returns: a List of integers
'''
from itertools import repeat 

def moving_zeroes(arr):
    zeros = arr.count(0)
    for i in range(len(arr)):
        if 0 in arr:
            arr.remove(0)
    
    arr.extend(repeat(0, zeros))
    
    return arr

if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")