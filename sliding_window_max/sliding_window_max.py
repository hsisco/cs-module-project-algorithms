'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(arr, k):      
    max_arr = []                        # create new array
    for i in range(len(arr) - k + 1):   # for the provided array without the k values (+ 1 to make it accurate)
        max_arr.append(max(arr[i:i+k])) # add to new array all values, skipping the k values in the span
    return max_arr                      # see what's in the new array

if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"\nOutput of sliding_window_max function is: {sliding_window_max(arr, k)}")