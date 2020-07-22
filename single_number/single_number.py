'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    for i in range(len(arr)):       # for all the i in the array:
        if arr.count(arr[i]) < 2:   # if the occurrance of i is only once:
            return arr[i]           # return it

if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"\nThe odd-number-out is {single_number(arr)}")