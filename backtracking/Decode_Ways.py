"""
date: 18/4/2022
no.: 91
topic: string, dynamic programming

################################################
question:
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
################################################

example:
Input: s = "12"
Output: 2
Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).

Input: s = "226"
Output: 3
Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

Input: s = "06"
Output: 0
Explanation: "06" cannot be mapped to "F" because of the leading zero ("6" is different from "06").

STRATEGY:
1. use backtracking, cause we need to go back to the previous string index to check if another combination is valid
2. before backtracking, conditions:
    a. make sure string is not 0, if it is just return 0
    b. if empty just return 1
3. condition to backtrack:
      if the first and second string is <= 26,
        then we backtrack the first and second string
4. when no backtracking is needed, go to the next character in the string
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


s = "26"
solution = Solution.numDecodings(s)
