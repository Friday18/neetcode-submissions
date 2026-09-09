class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False
        
        mapOfS = {}

        for i in s:
            mapOfS[i] = mapOfS.get(i,0)+1
        
        mapOfT = {}
        for i in t:
            mapOfT[i] = mapOfT.get(i, 0)+1
        
        return mapOfS == mapOfT