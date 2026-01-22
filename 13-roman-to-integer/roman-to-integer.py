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
        special_cases = ["IV", "IX", "XL", "XC", "CD", "CM"]
        while i < len(s):
            if i + 1 < len(s) and s[i:i+2] in special_cases:
                total += table[s[i+1]] - table[s[i]]
                i += 1
            else:
                total += table[s[i]]
            i += 1
        return total
        