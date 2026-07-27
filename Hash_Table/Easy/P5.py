# You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.
#
# Letters are case sensitive, so "a" is considered a different type of stone from "A".

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:

        jeweldict = dict()

        count = 0

        for a in jewels:

            jeweldict[a] = 1

        for b in stones:

            if b in jeweldict:

                count += 1

        return count
# This BigO(N) in space and Time