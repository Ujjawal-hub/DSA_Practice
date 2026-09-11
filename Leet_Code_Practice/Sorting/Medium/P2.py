# Given an array of intervals where intervals[i] = [starti, endi],
# merge all overlapping intervals, and return an array of the non-overlapping
# intervals that cover all the intervals in the input.

class Solution:

    def check(self,list1,list2):

        if list2[0] <= list1[1]:

            return [min(list1[0],list2[0]),max(list1[1],list2[1])]

        else:

            return None

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key = lambda x : x[0])

        i = 1

        answer = list()

        while len(intervals) >=2 and  i < len(intervals):

            y = self.check(intervals[i-1],intervals[i])

            if  isinstance(y,list):

                intervals[i] = y

            else:

                answer.append(intervals[i-1])

            i += 1

        answer.append(intervals[-1])




        return answer


    # this is BigO(Nlogn) and BigO(n) space