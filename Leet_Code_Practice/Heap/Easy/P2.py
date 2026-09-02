# You are given an array of integers stones where stones[i] is the weight of the ith stone.
#
# We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:
#
# If x == y, both stones are destroyed, and
# If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
# At the end of the game, there is at most one stone left.
#
# Return the weight of the last remaining stone. If there are no stones left, return 0.


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        for x in range(0,len(stones)):

            stones[x] = - stones[x]

        heapq.heapify(stones)


        while len(stones) >1:

            a = heapq.heappop(stones)
            b = heapq.heappop(stones)

            c = a - b

            if c != 0:

                heapq.heappush(stones,c)

        if len(stones) == 0:

            return 0

        else:

            return -stones[0]

    # BigO(nlogn) and BigO(1) in space

# this solution uses max heap actually , so but python butin have min heap,  s by stroing the values as -ve
# ,we can simulte max heap using min heap