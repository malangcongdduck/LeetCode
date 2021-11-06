class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count=0
        for j in jewels:
            for s in stones:
                if s==j:
                    count+=1
        return count