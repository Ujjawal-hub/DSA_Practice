# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# An input string is valid if:
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

class Solution:
    def isValid(self, s):

        dicti = {']': '[', ')': '(', '}': '{'}

        list1 = list()

        for a in s:

            if a in dicti.values():
                list1.append(a)

            if a in dicti:



                if len(list1) == 0:

                    return False

                else:

                    w = list1.pop()


                # try:
                #
                #     w = list1.pop()
                #
                #
                #
                # except:
                #
                #     return False

                if dicti[a] != w:
                    return False

        if len(list1) != 0:

            return False

        else:

            return True

# This is BigO(n) In space and time also