class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_dict = {}
        for c in s:
            s_dict[c] = s_dict.get(c, 0) + 1
        for c in t:
            try:
                s_dict[c] -= 1
                if s_dict[c] == 0:
                    del(s_dict[c])
            except KeyError:
                return False
        if s_dict == {}:
            return True

