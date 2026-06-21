class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort()
        count=defaultdict(int)
        n=len(hand)
        for i in range(len(hand)):
            count[hand[i]]+=1
        i=0
        for card in hand:
            if count[card]<=0:
                continue
            for j in range(card,card+groupSize):
                target=j
                if count[target]<=0:
                    return False
                count[target]-=1
        return True