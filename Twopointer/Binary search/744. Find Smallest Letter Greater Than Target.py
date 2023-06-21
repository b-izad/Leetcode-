'''744. Find Smallest Letter Greater Than Target

You are given an array of characters letters that is sorted in non-decreasing order, and a character target. There are at least two different characters in letters.

Return the smallest character in letters that is lexicographically greater than target. If such a character does not exist, return the first character in letters.

 

Example 1:

Input: letters = ["c","f","j"], target = "a"
Output: "c"
Explanation: The smallest character that is lexicographically greater than 'a' in letters is 'c'.
Example 2:

Input: letters = ["c","f","j"], target = "c"
Output: "f"
Explanation: The smallest character that is lexicographically greater than 'c' in letters is 'f'.'''

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:

        start = 0
        end = len(letters) - 1

        if target < letters[start] or target >= letters[end]:
            return letters[start]

        while start <= end:
            middle = start + (end - start) // 2
            candidate = letters[middle]

            if target < candidate:
                end = middle - 1

            if target >= candidate:
                start = middle + 1

        return letters[start]