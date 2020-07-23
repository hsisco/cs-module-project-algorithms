'''
Input: a List of integers
Returns: a List of integers
'''
def product_of_all_other_numbers(arr):
    l = len(arr)                            # create var, we'll be using this a lot
    
    before = [1] * l                        # create temp arrays, starting with 1
    after = [1] * l
    product = [0] * l

    for i in range(1, l):                   # create array of values before the selected element
        before[i] = before[i-1] * arr[i-1]  # multiply corresponding elements of before and arr

    for i in range(l - 2, -1, -1):          # create array of values after the selected element
        after[i] = after[i+1] * arr[i+1]    # multiply corresponding elements of after and arr

    for i in range(0, l):                   # create product array
        product[i] = before[i] * after[i]   # multiply corresponding elements of before and after

    return product                          # see what you got

if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"\nOutput of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")