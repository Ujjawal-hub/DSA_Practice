# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.
# #
# # For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# # Return true if you can finish all courses. Otherwise, return false.


class Solution:

    def edges_to_graph(self, edges):

        graph = dict()

        for edge in edges:

            b, a = edge

            if a in graph:

                graph[a].append(b)

            else:

                graph[a] = [b]

            if b not in graph:
                graph[b] = list()

        return graph

    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:

        graph = self.edges_to_graph(prerequisites)

        visited = set()

        for start in graph:

            if start not in visited:

                path = set()

                Bool = self.dfs(start, visited, graph, path)

                if Bool == False:
                    return False

        return True

    def dfs(self, start, visited, graph, path):

        visited.add(start)

        path.add(start)

        for i in graph[start]:

            if i not in visited:

                Bool = True

                Bool = self.dfs(i, visited, graph, path)

                if Bool == False:
                    return False

            elif i in path:

                return False

        path.remove(start)

# basically here we should be able to do topologicla sort
# so if there is a cycle present then topological sort is not possible
# this is BigO(N+len(prerequisites)) in Both space and time,where N is total number of unique elements, representing vertices or number of courses,and len(prequesites) is number of edges