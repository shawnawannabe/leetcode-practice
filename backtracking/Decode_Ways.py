"""
No.: 91
Topic: string, dynamic programming

################################################
Question:
A message containing letters from A-Z can be encoded into numbers using the following mapping:
'A' -> "1"
'B' -> "2"
...
'Z' -> "26"
To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, "11106" can be mapped into:
"AAJF" with the grouping (1 1 10 6)
"KJF" with the grouping (11 10 6)
Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".
Given a string s containing only digits, return the number of ways to decode it.
The test cases are generated so that the answer fits in a 32-bit integer.

Constraints:
1 <= s.length <= 100
s contains only digits and may contain leading zero(s).

Example:
Input: s = "12"
Output: 2
Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).

Input: s = "226"
Output: 3
Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

Input: s = "06"
Output: 0
Explanation: "06" cannot be mapped to "F" because of the leading zero ("6" is different from "06").
################################################

Approach:
1. use backtracking (an algorithm), cause we need to go back and forth to see if the second char is able to form a combination with the following char, 
    eg. 261, has 4 combi [2,26,6,1]
        271, has 3 combi [2,7,1]
    6 is able to form a combi with the previous number 2, whereas 7 is unable to
2.  edge cases:
    a. is string empty, return 0
3. how to backtrack:
    a. take the first and second char of the string for comparison
        a1. if the first char is 0, return 0 straight away, why, refer Example 3 above
        a2. if len(string) is 1, return 1, why, cause 1-9 can only have 1 combi
        a3. if string is "", return 1, why, cause the string has already reached the end of the function
        a4. if the int of the first and second char is lower or equal to 26, go through the function once again with the first char and second char differently, why, refer to Approach 1 second eg.
        a5. else, (which means 4 of the example is not feasible, eg. string = 27), no backtracking is needed, just loop through the function with the second char only (in this case 7)

Layman's term (may deleted later)
1. use backtracking (it's an algorithm), cause we need to go back to the previous string index to check if another combination is valid
2. before backtracking, conditions:
    a. make sure string is not 0, if it is just return 0
    b. if empty just return 1
3. condition to backtrack:
      if the first and second string is <= 26,
        then we backtrack the first and second string
4. when no backtracking is needed (aka the first two char is > 26), go to the second character in the string
"""

from functools import lru_cache


class Solution:
    def __init__(self):
        pass

    def numDecodings(s: str) -> int:
        if len(s) == 0 or s is None:
            return 0

        @lru_cache
        def dfs(string):
            if len(string) > 0:
                if string[0] == '0':
                    return 0
            if string == "" or len(string) == 1:
                return 1
            if int(string[0:2]) <= 26:
                first = dfs(string[1:])
                second = dfs(string[2:])
                return first+second
            else:
                return dfs(string[1:])

        result_sum = dfs(s)
        print(result_sum)

        return result_sum


s = "27"
solution = Solution.numDecodings(s)
