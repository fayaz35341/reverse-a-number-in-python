class Solution:
    def reverseNumber(self, n):
        a=list(str(n))
        b=(a[::-1])
        return int(''.join(map(str, b)))
print(Solution().reverseNumber(74))
