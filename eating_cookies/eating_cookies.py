'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n):
    if n < 0:
        return 0
    if n == 0:
        return 1
    combos = eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)
    
    return combos

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5
    print(f"\nThere are {eating_cookies(num_cookies)} ways for Cookie Monster to eat {num_cookies} cookies")

    num_cookies = 23
    print(f"\nThere are {eating_cookies(num_cookies)} ways for Cookie Monster to eat {num_cookies} cookies")