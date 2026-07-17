# You are keeping the scores for a baseball game with strange rules. At the beginning of the game, you start with an empty record.
#
# You are given a list of strings operations, where operations[i] is the ith operation you must apply to the record and is one of the following:
#
# An integer x.
# Record a new score of x.
# '+'.
# Record a new score that is the sum of the previous two scores.
# 'D'.
# Record a new score that is the double of the previous score.
# 'C'.
# Invalidate the previous score, removing it from the record.
# Return the sum of all the scores on the record after applying all the operations.


class Solution:
    def calPoints(self, operations):

        list1 = list()

        i = 0

        for a in operations:

            try:

                b = int(a)

                list1.append(b)

            except:

                if len(list1) >= 1:

                    match a:

                        case '+':

                            if len(list1) > 1:

                                b = list1.pop()
                                c = list1.pop()
                                d = b + c

                                list1.extend([c, b, d])


                            else:

                                b = list1.pop()
                                list1.extend([b, b])

                        case 'D':

                            b = list1.pop()

                            list1.extend([b, b * 2])

                        case 'C':

                            list1.pop()

            print(list1)

        return sum(list1)

# This is BigO(n) in both space and time