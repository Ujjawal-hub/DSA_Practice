# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
#
# Each letter in magazine can only be used once in ransomNote.

class Solution:
    def canConstruct(self, ransomNote, magazine) :

        magdict = dict()

        for a in magazine:

            if a in magdict:

                magdict[a] += 1

            else:

                magdict[a] = 1

        for b in ransomNote:

            if b in magdict and magdict[b] != 0:

                magdict[b] -= 1
            else:

                return False

        return True

# This is BigO(N) in Both space and time