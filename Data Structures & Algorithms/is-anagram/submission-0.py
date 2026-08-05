class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        string1 = {} # char : number of reps
        string2 = {}

        for char in s:
            if char not in string1:
                string1[char] = 0
            else:
                string1[char] += 1

        for char in t:
            if char not in string2:
                string2[char] = 0
            else:
                string2[char] += 1

        if string1 == string2:
            return True
        else:
            return False
        