class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False
        
        mapOfS = {}

        for i in s:
            mapOfS[i] = mapOfS.get(i,0) + 1
        
        for i in t:
            mapOfS[i] = mapOfS.get(i, 0) - 1
        a = all(val == 0 for val in mapOfS.values())
        return a