class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        res=[0,0,0]
        for x in triplets:
            if x[0]>target[0] or x[1]>target[1] or x[2]>target[2]:
                continue
            else:
                ai=x[0]
                bi=x[1]
                ci=x[2]
                aj=res[0]
                bj=res[1]
                cj=res[2]
                res=[max(ai, aj), max(bi, bj), max(ci, cj)]
                if res==target:
                    return True
        return False