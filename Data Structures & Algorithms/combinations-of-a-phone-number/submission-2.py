class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        res=[]
        letter=defaultdict(list)
        c=97
        for i in range(2,10):
            if i==7 or i==9:
                for j in range(4):
                    letter[str(i)].append(str(chr(c)))
                    c+=1
            else:
                for j in range(3):
                    letter[str(i)].append(str(chr(c)))
                    c+=1
        
        def lcomb(curr, i):
            if i==len(digits):
                res.append(curr[::])
                return
            for j in range(len(letter[digits[i]])):
                lcomb(curr+letter[digits[i]][j],i+1)

        lcomb("",0)
        return res