class Solution:
    def romanToInt(self, s: str) -> int:
        table ={
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        total = 0
        i = 0
        while i < len(s):
            if s[i:i+2] in ["IV", "IX", "XL", "XC", "CD", "CM"] and s[i+1]:
                total += table[s[i+1]] - table[s[i]]
                i += 1
            else:
                total += table[s[i]]
            i += 1
        return total
        