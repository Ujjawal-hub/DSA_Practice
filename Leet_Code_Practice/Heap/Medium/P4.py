#You are given an array of CPU tasks, each labeled with a letter from A to Z, and a number n. Each CPU interval can be idle or allow the completion of one task. Tasks can be completed in any order, but there's a constraint: there has to be a gap of at least n intervals between two tasks with the same label.

#Return the minimum number of CPU intervals required to complete all tasks.
#

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        count = Counter(tasks)

        h = [-freq for item, freq in count.items()]

        heapq.heapify(h)

        no = 0

        f = 0

        queue = list()

        while h:

            while no <= n:

                if len(h) == 0 and len(queue) == 0:
                    break

                if len(h) != 0:

                    q = heapq.heappop(h) + 1

                    if q != 0:
                        queue.append(q)

                no += 1

                f += 1

            no = 0

            h.extend(queue)

            heapq.heapify(h)

            queue = []

        return f

        # this is BigO(nlogn) in Time and BigO(1) in space

    #Greedy Math Approach

class Solution:

  def leastInterval(self, tasks: List[str], n: int) -> int:
    counts = Counter(tasks).values()
    max_freq = max(counts)

    # Count how many tasks share the maximum frequency
    max_freq_count = sum(1 for f in counts if f == max_freq)

    # Calculate empty spaces based on max frequency task blocks
    # Formula: (max_freq - 1) * (n + 1) + max_freq_count
    intervals = (max_freq - 1) * (n + 1) + max_freq_count

    # Answer is either the calculated interval grid OR array length (if no idles needed)
    return max(len(tasks), intervals)

  # this is BigO(n) in Time and BigO(1) in space