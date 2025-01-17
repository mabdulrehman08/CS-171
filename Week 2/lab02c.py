# Recursive function to check if a number is odd without using %
def num_is_odd(num):
    if num == 0:
        return False  # Even
    if num == 1:
        return True  # Odd
    return num_is_odd(num - 2)

# Function to count odd numbers among five inputs
def countOdds(num1, num2, num3, num4, num5):
    return (num_is_odd(num1) + 
            num_is_odd(num2) + 
            num_is_odd(num3) + 
            num_is_odd(num4) + 
            num_is_odd(num5))

# Main block to test the function
if __name__ == '__main__':
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())
    num4 = int(input())
    num5 = int(input())
    result = countOdds(num1, num2, num3, num4, num5)
    print(f'Total odds: {result}')
