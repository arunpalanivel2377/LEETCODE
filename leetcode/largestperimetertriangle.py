"""
976. Largest Perimeter Triangle
Easy
Topics
premium lock icon
Companies
Given an integer array nums, return the largest perimeter of a triangle with a non-zero area, formed from three of these lengths. If it is impossible to form any triangle of a non-zero area, return 0.

 

Example 1:

Input: nums = [2,1,2]
Output: 5
Explanation: You can form a triangle with three side lengths: 1, 2, and 2.
Example 2:

Input: nums = [1,2,1,10]
Output: 0
Explanation: 
You cannot use the side lengths 1, 1, and 2 to form a triangle.
You cannot use the side lengths 1, 1, and 10 to form a triangle.
You cannot use the side lengths 1, 2, and 10 to form a triangle.
As we cannot use any three side lengths to form a triangle of non-zero area, we return 0.
 

Constraints:

3 <= nums.length <= 104
1 <= nums[i] <= 106
"""


def largest(nums:list[int]) -> int: # [1,2,10,1]
    
    nums.sort(reverse=True) # [10,2,1,1]
    largest = 0
    for i in range(0,len(nums)-2): # 0
        c = nums[i] # 0 10
        b = nums[i + 1] # 1 2
        a = nums[i + 2] # 2 1
        perimeter = a + b + c
        if a + b > c: # triangle inequality theorem 3 < 10
            if largest < perimeter:
                largest = perimeter
    return largest
            
print(largest([1,2,10,1]))
print(largest([2,1,2]))
print(largest([1,5,7,9,5]))

