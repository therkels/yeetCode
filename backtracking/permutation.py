# Function to swap characters in a string
def swap(s, i, j):
    s = list(s)
    s[i], s[j] = s[j], s[i]
    return ''.join(s)

# Function to print permutations of the string
# This function takes two parameters:
# 1. String
# 2. Starting index of the string.
def permuteRec(s, idx):
  
    # Base case
    if idx == len(s) - 1:
        print(s)
        return
    
    for i in range(idx, len(s)):
      
        # Swapping
        s = swap(s, idx, i)

        # First idx+1 characters fixed
        permuteRec(s, idx + 1)

        # Backtrack
        s = swap(s, idx, i)

# Wrapper function
def permute(s):
    permuteRec(s, 0)

# Driver code
s = "ABC"
permute(s)