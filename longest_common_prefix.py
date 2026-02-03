class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        for x in range(len(strs[0])):
            char = strs[0][x]
            for s in strs[1:]:
                if x >=len(s) or s[x] != char:
                    return strs[0][:x]
        return strs[0]
