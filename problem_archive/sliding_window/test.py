def calculate_ratio(numerator, denominator):
    # Assert that the denominator is not zero
    assert denominator != 0, "Denominator cannot be zero"
    
    ratio = numerator / denominator
    return ratio

# Example variables
num = 10
denom = 0

# This will hit the assert because the denominator is zero
result = calculate_ratio(num, denom)
print("Ratio:", result)