# Given an array of integers temperatures represents the daily
# temperatures, return an array answer such that answer[i] is the number of
# days you have to wait after the ith day to get a warmer temperature.
# If there is no future day for which this is possible,
#     keep answer[i] == 0 instead.

from collections import deque


class Solution:
    def dailyTemperatures(self, temperatures):

        list1 = deque()   # it will store temprature
        list2 = deque()   # it will store day of temp mapped  to #positions of list1
        answers = [None]*len(temperatures)
        Dayindex = 0

        for a in temperatures:

            if len(list1) == 0:

                list1.append(a)
                list2.append(Dayindex)
            else:

                while list1[-1] < a:

                    temp = list1.pop()
                    day = list2.pop()

                    number_of_days = Dayindex - day

                    answers[day] = number_of_days

                    if len(list1) == 0:

                        break

                list1.append(a)
                list2.append(Dayindex)

            Dayindex += 1

        while len(list2) !=0:

            day = list2.pop()

            answers[day] = 0

        return answers

# This solution is BigO(N) in both space and time

# here instead of maintaing two stack i could have done in one , if i use tuple
#(temperature,day) to store in the stack