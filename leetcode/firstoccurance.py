"""
28. Find the Index of the First Occurrence in a String
Solved
Easy
Topics
premium lock icon
Companies
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

 

Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
"""

# Brute force:
"""def strStr(haystack: str, needle: str) -> int:
    index = -1
    for i in range(len(haystack)): 
        if needle[0] == haystack[i]:
            j = 0 
            counter = 0
            start = i
            while j < len(needle): # 5
                if needle[j] == haystack[i]:
                    i = i +1
                    j = j +1
                    counter +=1 
                else:
                    j = j +1
            if counter == len(needle):
                index = start
                return
            else:
                index = -1
    return index
print(strStr("sadbutsad","sad"))
print(strStr("leetcode","leeto"))


"""

# Brute force cleaner version:

def strStr(haystack: str, needle: str) -> int:
    n,m = len(haystack), len(needle)

    for i in range(n-m+1):
        match = True
        for j in range(m):
            if haystack[i+j] != needle[j]:
                match = False
                break
        if match:
            return i
    return -1

print(strStr("sadbutsad","sad"))
print(strStr("leetcode","leeto"))