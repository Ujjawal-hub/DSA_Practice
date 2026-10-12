#A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

# Every adjacent pair of words differs by a single letter.
# Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
# sk == endWord
# Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:

        pattern_dict = dict()

        queue = deque()

        visited = set()

        for word in wordList:

            for i in range(0,len(word)):

                pattern = word[0:i] + "*" + word[i+1:len(word)]

                if pattern in pattern_dict:

                    pattern_dict[pattern].append(word)

                else:

                    pattern_dict[pattern] = [word]



        queue.append(beginWord)

        count = 1

        while queue:

            iterations = len(queue)

            count += 1

            while iterations > 0:

                word = queue.popleft()

                for i in range(0,len(word)):

                    pattern = word[0:i] + "*" + word[i+1:len(word)]

                    if pattern in visited:

                        continue

                    if pattern not in pattern_dict:

                        continue

                    List = pattern_dict[pattern]

                    for letter in List:

                        queue.append(letter)

                        if letter == endWord:

                            return count

                    visited.add(pattern)

                iterations -= 1

        return 0


# this solution is BigO(N*L^2) in Both Space and Time , where N is number of words ,L is number od characrters in each word , forming L patterns , total N*L patterns and each one is of space L , for time for each deque look L times in dictionary