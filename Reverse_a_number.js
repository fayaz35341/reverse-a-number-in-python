
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
