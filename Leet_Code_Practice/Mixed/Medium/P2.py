# Given an encoded string, return its decoded string.
#
# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.
#
# You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].
#
# The test cases are generated so that the length of the output will never exceed 105.


class Solution:
    def decodeString(self, s: str) -> str:

        list1 = deque()
        result = ""
        openbraces = 0

        for a in s:

            if a == "[":

                b = ""

                while len(list1) != 0 and list1[-1].isdigit():
                    c = list1.pop()
                    # b = b+c or b +=c
                    # not this b = b +c because it will create wrong sequence
                    b = c + b

                list1.append(int(b))
                list1.append(a)
                openbraces += 1

            elif a == "]":

                b = ""

                while list1[-1] != "[":
                    c = list1.pop()

                    # not this b = b +c because it will create wrong sequence
                    b = c + b

                list1.pop()

                d = list1.pop()

                e = d * b

                openbraces -= 1

                if openbraces == 0:

                    result += e

                else:

                    list1.append(e)

            elif a.isdigit():

                list1.append(a)

            else:

                if openbraces == 0:

                    result += a


                else:

                    list1.append(a)

        return result

# this is BigO(M) in both space and Time and here M is Output number of charcters
