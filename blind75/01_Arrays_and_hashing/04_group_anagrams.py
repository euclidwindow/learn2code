# group words with similar alphabets

# SOLUTION 1 : TC: O(n), SC: O(n)

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for word in strs:
            key = "".join(sorted(word))
            if key in hashmap.keys():
                hashmap[key].append(word)
            else:
                hashmap[key] = [word]
        return hashmap.values()
