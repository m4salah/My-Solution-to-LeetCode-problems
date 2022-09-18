class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        res = {}
        for c in s:
            res[c] = res.get(c, 0) + 1
        
        for c in t:
            if c in res:
                if res[c] == 0:
                    return False
                res[c] -= 1
            else:
                return False
        return True
            
                