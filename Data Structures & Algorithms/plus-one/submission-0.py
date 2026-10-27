class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ans=0
        for digit in digits:
            ans*=10
            ans+=digit
        ans+=1
        arr=[]
        while(ans!=0):
            arr.append(ans%10)
            ans//=10
        return arr[::-1]