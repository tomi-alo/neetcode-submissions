from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += f"{len(s)}#{s}"
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        
        while i < len(s):
            # Find where the length prefix ends
            j = i
            while s[j] != '#':
                j += 1
            
            length = int(s[i:j])
            # Extract the actual string using the parsed length
            res.append(s[j + 1 : j + 1 + length])
            # Move index to the start of the next length-prefix
            i = j + 1 + length
            
        return res