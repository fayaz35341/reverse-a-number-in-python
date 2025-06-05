# class Solution:
#     def reverseNumber(self, n):
#         a=list(str(n))
#         b=(a[::-1])
#         return int(''.join(map(str, b)))
# print(Solution().reverseNumber(74))

# python
class Solution:
    def reverseNumber(self, n):
        reverse_num=0
        while n>0:
            ld=int(n%10)
            reverse_num=int(reverse_num*10)+ld
            n=int(n/10)
        return reverse_num
print(Solution().reverseNumber(745497))

# JS

class Solution {
    reverseDigits(n) {
        // code here
        let reverse_num=0
        while (n>0){
            let ld=(n%10)
            reverse_num=(reverse_num*10)+ld
            n=Math.floor(n/10)
        }
        return reverse_num
    }
}
console.log(new Solution().reverseDigits(123))
