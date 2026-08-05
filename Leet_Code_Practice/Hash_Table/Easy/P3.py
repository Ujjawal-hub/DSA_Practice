#Given two strings s and t, return true if t is an anagram of s, and false otherwise.
#Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        anagram = dict()

        for a in s:

            if a in anagram:

                anagram[a] += 1
            else:

                anagram[a] = 1

        for a in t:

            if a in anagram:

                anagram[a] -= 1

                if anagram[a] == 0:
                    anagram.pop(a)

            else:

                return False

        # python treat empty object as false

        if anagram:
            return False

        return True
# This is BigO(N) in Both sapce and Time