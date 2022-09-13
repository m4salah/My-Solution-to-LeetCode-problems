class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        for i, c in enumerate(s):
            if c in d:
                d[c] = -1
            else:
                d[c] = i
        
        for key in d:
            if d[key] != -1:
                return d[key]
        return -1