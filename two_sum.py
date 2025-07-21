# 
# two_sums.py
#
# Created: 3 Jul 2025
# Edited:  3 Jul 2025
#
# Version 1.0
# Andwardo
#

def two_sum(nums, target):
    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
    return []

# --- User Input Section ---
nums_input = input("Enter numbers separated by commas (e.g., 2,7,11,15): ")
target_input = input("Enter target sum (e.g., 9): ")

# Convert input to usable format
nums = list(map(int, nums_input.strip().split(',')))
target = int(target_input.strip())

# Compute result
result = two_sum(nums, target)
print(f"Indices of numbers that add to {target}: {result}")
