class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        right=len(matrix[0])
        left=0
        down=len(matrix)
        up=0
        res=[]

        while(left<right and up<down):
            for k in range(left,right):
                res.append(matrix[up][k])
            up+=1
            for k in range(up,down):
                res.append(matrix[k][right-1])
            right-=1
            if not(left<right and up<down):
                break
            for k in range(right-1,left-1,-1):
                res.append(matrix[down-1][k])
            down-=1
            for k in range(down-1,up-1,-1):
                res.append(matrix[k][left])
            left+=1
        return res
    