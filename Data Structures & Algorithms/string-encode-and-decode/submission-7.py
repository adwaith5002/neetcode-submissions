class Solution:
    def encode(self, strs: List[str]) -> str:
        S=[]
        for i in strs:
            S.append(str(len(i)))
            S.append('#')
            S.append(i)
        return "".join(S)
    def decode(self, s: str) -> List[str]:
        L=[]
        i=0
        while(i<len(s)):
            j=i
            while(s[j]!='#'):
                j+=1
            length=int(s[i:j])
            i=j+1
            L.append(s[i:i+length])
            i=i+length
        return L