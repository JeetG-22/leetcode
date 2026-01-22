class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i = len(s) - 1
        j = 0
        while i > j:
            temp = s[i]
            s[i] = s[j]
            s[j] = temp
            i -= 1
            j += 1
        return s

        