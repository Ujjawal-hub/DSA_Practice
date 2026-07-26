# You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.
#
# Evaluate the expression. Return an integer that represents the value of the expression.
#
# Note that:
#
# The valid operators are '+', '-', '*', and '/'.
# Each operand may be an integer or another expression.
# The division between two integers always truncates toward zero.
# There will not be any division by zero.
# The input represents a valid arithmetic expression in a reverse polish notation.
# The answer and all the intermediate calculations can be represented in a 32-bit integer.
from collections import deque

class Solution:

    def twopop(self,list1):

        a = list1.pop()
        b = list1.pop()

        # returning in the right sequence

        return (b,a)


    def evalRPN(self, tokens):

        list1 = deque()

        for a in tokens:

            try:

                b = int(a)

                list1.append(b)

            except:

                match a:

                    case '+':

                        (c,d) = self.twopop(list1)

                        e = c+d

                        list1.append(e)

                    case '-':

                        (c,d) = self.twopop(list1)

                        e = c-d

                        list1.append(e)

                    case '*' :

                        (c,d) = self.twopop(list1)

                        e = c*d

                        list1.append(e)

                    case '/':

                        (c,d) = self.twopop(list1)

                        e = int(c/d)



                        list1.append(e)

        return list1.pop()

    #This is BigO(n) in Both Time and space