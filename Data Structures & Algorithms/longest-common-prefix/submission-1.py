class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        str_to_return = ""
        for i, c in enumerate(strs[0]):
            for s in strs[1:]:
                if s[i:i+1] != c:
                    return str_to_return
            str_to_return += c
        return str_to_return