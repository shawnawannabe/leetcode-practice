"""
No: 49
Topic: hash table, string, sorting

#######################################################
Question:
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Input: strs = [""]
Output: [[""]]

Input: strs = ["a"]
Output: [["a"]]

Constraints:
1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
#######################################################

Approach:
1. Just use a hash table data structure to solve this
2. The key would be the same for all anagram after sorting, 
    eg. ["ate", "eat"] would have the same key "aet"
    note: hash table aka dictionary will only have one key, 
        a. property of dictionary: https://www.tutorialspoint.com/python_data_structure/python_dictionary_data_structure.htm#:~:text=Keys%20are%20unique%20within%20a%20dictionary%20while%20values%20may%20not%20be.%20The%20values%20of%20a%20dictionary%20can%20be%20of%20any%20type%2C%20but%20the%20keys%20must%20be%20of%20an%20immutable%20data%20type%20such%20as%20strings%2C%20numbers%2C%20or%20tuples.
        b. some info on hash table: https://www.tutorialspoint.com/python_data_structure/python_hash_table.htm#:~:text=Hash%20tables%20are,a%20hashing%20function
3. By utilizing the same key, we can group the anagram together
4. To get the desired result, just return the value of the hashtable
"""

# defaultdict is a sub class of dictionaries in python
# properties of default dict: it never raises a KeyError
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs):
        d = defaultdict(list)

        for s in strs:
            key = "".join(sorted(s))
            # print(key)
            d[key].append(s)
            # print("keys: ", d.keys())
            # print("values:", d.values())
        return d.values()


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
solution = Solution().groupAnagrams(strs)
