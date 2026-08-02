# Given an array of strings strs, group the anagrams together.
# You can return the answer in any order.

# class Solution:
#
#     def isAnagram(self, string1, string2):
#
#         anagramdict = dict()
#
#         if len(string1) != len(string2):
#             return False
#
#         for a in string1:
#
#             if a in anagramdict:
#
#                 anagramdict[a] += 1
#             else:
#
#                 anagramdict[a] = 1
#
#         for b in string2:
#
#             if b in anagramdict:
#
#                 anagramdict[b] -= 1
#
#                 if anagramdict[b] == 0:
#                     anagramdict.pop(b)
#             else:
#
#                 return False
#
#         return True
#
#     def groupAnagram_Jr(self, strs):
#
#         a = list()
#         b = list()
#         b.append(strs[0])
#         a.append(b)
#
#         i = 1
#
#         while i < len(strs):
#
#             j = 0
#
#             while j < len(a):
#
#                 if self.isAnagram(a[j][0], strs[i]):
#                     a[j].append(strs[i])
#
#                     break
#
#                 j += 1
#
#             else:
#
#                 b = [strs[i]]
#
#                 a.append(b)
#
#             i += 1
#
#         return a
#
#     def groupAnagrams(self, strs) :
#
#         lendict = dict()
#
#         answer = list()
#
#         for a in strs:
#
#             if len(a) in lendict:
#
#                 # lendict[len(a)] = lendict[len(a)].append(a)  wrong key is just a pointer to list apeend will retun none so pointer will point to none
#
#                 lendict[len(a)].append(a)
#
#             else:
#
#                 lendict[len(a)] = [a]
#
#         for b in lendict:
#
#             array = self.groupAnagram_Jr(lendict[b])
#
#             for i in array:
#                 answer.append(i)
#
#         return answer

 #this is BigO((N^2)*k) in Time and BigO(N) in space (if we traet a string as a single unit of space) otherwise it is BigO(Nk),where N is number of string in the l=array and k is number of character in the string






# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#
#         groupdict = dict()
#
#         for string in strs:
#
#             key = "".join(sorted(string))
#
#             if key in groupdict:
#
#                 groupdict[key].append(string)
#
#             else:
#
#                 groupdict[key] = [string]
#
#         answer = list()
#
#         for a in groupdict:
#
#             answer.append(groupdict[a])
#
#         return answer

# this is BigO(Nklogk) due to sorting of klogk per string

import string


class Solution:

    def __init__(self):

        self.hashdict = dict()

        for i in string.ascii_lowercase:
            self.hashdict[i] = None

    def hashkey(self, strin):

        for i in strin:

            if self.hashdict[i] == None:

                self.hashdict[i] = 1
            else:

                self.hashdict[i] += 1

                # k operation

        a = str(self.hashdict)

        for i in strin:
            self.hashdict[i] = None

            # k operation

        return a

    def groupAnagrams(self, strs):

        groupdict = dict()

        for strin in strs:

            key = self.hashkey(strin)

            # k opertaion per string

            if key in groupdict:

                groupdict[key].append(strin)

            else:

                groupdict[key] = [strin]

        answer = list()

        for a in groupdict:
            answer.append(groupdict[a])

        return answer

        # BigO(Nk) operation in time and BigO(Nk) in space also

    # in the standers solution instead of using dictionary as key ,
    # we use tuple, same concept a 26 length array , in which each index position is represented as a character a to z
    # we simply do +1 in that index position representing a particular character ,as index position of charcter remain same across differnt string, so two anagram always produces same list pattern  ,
    #here is he standers soulution

    # def groupAnagrams(self, strs):
    #     groupdict = dict()
    #
    #     for string in strs:
    #
    #         # Step 1: create empty count array of 26 zeros
    #         # index 0 = 'a', index 1 = 'b', ... index 25 = 'z'
    #         key = [0] * 26
    #
    #         # Step 2: for each character, increment its fixed index
    #         for c in string:
    #             key[ord(c) - ord('a')] += 1
    #
    #         # Step 3: convert to tuple so it can be used as dict key
    #         # lists are not hashable, tuples are
    #         key = tuple(key)
    #
    #         # Step 4: group by key
    #         if key in groupdict:
    #             groupdict[key].append(string)
    #         else:
    #             groupdict[key] = [string]
    #
    #     answer = list()
    #     for a in groupdict:
    #         answer.append(groupdict[a])
    #
    #     return answer


