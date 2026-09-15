class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Sort s and t, since the letter's frequency is same everywhere therefore they would be the same string.
        return "".join([chr(j) for j in sorted([ord(i) for i in s])]) == "".join([chr(j) for j in sorted([ord(i) for i in t])])


        
        
