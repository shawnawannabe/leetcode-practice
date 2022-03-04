"""
date: 4/3/22
question: 49
topic: hash table, string, sorting

we need it to return an array of anagram
approach:
1. just use a hash table data structure to solve this
2. the key would be the same for all anagram after sorting, 
  eg. ["ate", "eat"] would have the same key "aet"
3. by utilizing the same key, we can group the anagram together
4. to get the desired result, just return the value of the hashtable
"""


from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)

        for s in strs:
            key = "".join(sorted(s))
            d[key].append(s)
        return d.values()
