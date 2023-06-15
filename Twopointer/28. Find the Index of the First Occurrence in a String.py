'''28. Find the Index of the First Occurrence in a String
Easy

Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

 

Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.'''

def strStr(haystack, needle):
    if not needle:
        return 0

    i = j = 0
    start = 0
    while i < len(haystack) and j < len(needle):
        if haystack[i] == needle[j]:
            i += 1
            j += 1
        else:
            j = 0
            start += 1
            i = start

    if j == len(needle):
        return start
    else:
        return -1
