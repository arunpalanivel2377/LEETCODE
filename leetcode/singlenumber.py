"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

 

Example 1:

Input: nums = [2,2,1]

Output: 1

Example 2:

Input: nums = [4,1,2,1,2]

Output: 4

Example 3:

Input: nums = [1]

Output: 1

 

Constraints:

1 <= nums.length <= 3 * 104
-3 * 104 <= nums[i] <= 3 * 104
Each element in the array appears twice except for one element which appears only once.
"""

# Brute Force:

"""
Iterate through the each element and if it appears twice and
if it doesn't appear twice then return the element.
"""
def singleNumber(nums: list[int]) -> int:
    
    for i in nums:
        if nums.count(i) == 1:
            return i
        
print(singleNumber([2,2,1]))
print(singleNumber([4,1,2,1,2]))


# Optimized solution
"""
Use XOR:
    a ^ 0 = a
    a ^ a = 0
    single pass it check each and every element and runs on O(n) time complexity.

"""

def singleNumber1(num: list[int]) -> int:
    res = 0
    for i in num:
        res ^= i
    return res

print(singleNumber1([2,2,1]))
print(singleNumber1([4,1,2,1,2]))

