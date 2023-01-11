import heapq
class Solution(object):
    def lastStoneWeight(self, stones):
        while len(stones) >= 1:
            if len(stones) == 1:
                return stones[0]
            else:
                i = heapq.nlargest(2,stones)[0]
                j = heapq.nlargest(2,stones)[1]
                if heapq.nlargest(2,stones)[0] == heapq.nlargest(2,stones)[1]:
                    stones.remove(i)
                    stones.remove(j)
                
                else:
                    a = heapq.nlargest(2,stones)[0] - heapq.nlargest(2,stones)[1]
                    stones.append(a)
                    stones.remove(i)
                    stones.remove(j)
        if len(stones) == 0:
            return 0
        else:        
            return stones[0]
        """
        :type stones: List[int]
        :rtype: int
        """
