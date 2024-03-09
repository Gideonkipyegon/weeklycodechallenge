def divisible_by_ten(num):
    if num % 10 == 0:
        return True
    else:
        return False

# Test the function
print(divisible_by_ten(25))   # Output: False
print(divisible_by_ten(100))  # Output: True
print(divisible_by_ten(0))    # Output: True
