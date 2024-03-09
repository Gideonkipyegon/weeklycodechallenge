def large_power(base, exponent):
    result = base ** exponent
    if result > 5000:
        return True
    else:
        return False

# Test the function
print(large_power(.5, 3))  # Output: False
print(large_power(5, 4))   # Output: False
print(large_power(2, 10))  # Output: True
