from collections import deque


def dfs_graph_R(start, graph, visited):
    visited.add(start)

    print(start)

    i = 0

    while i < len(graph[start]):

        vertex = graph[start][i]

        if vertex not in visited:
            dfs_graph_R(vertex, graph, visited)

        i += 1

    return


# this is BigO(e + v) in Time and BigO(v) in space

def dfs(graph):  # this function call dfs recursicve version and give visited data set to function aslo check number of component

    visited = set()

    for i in graph:

        if i not in visited:
            dfs_graph_R(i, graph, visited)

    return


# even after adding comopnent part time and space is still same as dfs recursion

def dfs_iter(graph):
    stack = deque()

    visited = set()

    stack.append((0, 0))

    visited.add(0)

    print(0)
    while stack:

        vertex, index = stack[-1]

        i = index

        List = graph[vertex]

        while i < len(List):

            if List[i] not in visited:
                visited.add(List[i])

                print(List[i])

                stack.pop()

                stack.append((vertex, i + 1))

                stack.append((List[i], 0))

                break

            i += 1

        if i >= len(List):
            stack.pop()


# this is BigO(e + v) in Time and BigO(v) in space


def bfs_implemnt(graph):
    visited = set()

    queue = deque()

    visited.add(0)

    queue.append(0)

    while queue:

        vertex = queue.popleft()

        print(vertex)

        for i in graph[vertex]:

            if i not in visited:
                visited.add(i)

                queue.append(i)


# this is BigO(e + v) in Time and BigO(v) in space


matrix = [
    [0, 1, 1, 0, 0, 0],
    [1, 0, 0, 1, 1, 0],
    [1, 0, 0, 0, 0, 1],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 1],
    [0, 0, 1, 0, 1, 0]
]


def bfs_matrix(matrix):
    visited = set()

    queue = deque()

    visited.add(0)

    queue.append(0)

    while queue:

        vertex = queue.popleft()
        print(vertex)
        index = 0

        for i in matrix[vertex]:

            if i == 1:

                if index not in visited:
                    queue.append(index)

                    visited.add(index)

            index += 1

        # this solution is BigO(v**2) in Time and BigO(v) in space


def dfs_cycle_UN(graph):
    visited = set()

    return dfs_graph_C(0, graph, visited, None)


def dfs_graph_C_UN(start, graph, visited, parent):
    visited.add(start)

    i = 0

    while i < len(graph[start]):

        vertex = graph[start][i]

        if vertex not in visited:

            Bool = dfs_graph_C_UN(vertex, graph, visited, start)

            if Bool == True:
                return True

        elif vertex != parent:

            return True

    i += 1

    return False


# this is BigO(e + v) in Time and BigO(v) in space

def dfs_c_d(graph):
    path = set()
    visited = set()

    return dfs_graph_c_D(0, graph, visited, path)


def dfs_graph_c_D(start, graph, visited, path):
    visited.add(start)
    path.add(start)

    i = 0

    while i < len(graph[start]):

        vertex = graph[start][i]

        if vertex not in visited:

            Bool = dfs_graph_c_D(vertex, graph, visited, path)

            if Bool == True:
                return True

        elif vertex in path:

            return True

        i += 1

    path.remove(start)

    return False


# this is BigO(e + v) in Time and BigO(v) in space

def topological_sort(graph):
    path = set()
    visited = set()
    sort = list()

    for i in graph:

        if i is not in visited:

            Bool = dfs_graph_c_D_T(i, graph, visited, path, sort)

            if Bool == True:
                return None

    sort.reverse()

    return sort


def dfs_graph_c_D_T(start, graph, visited, path, sort):
    visited.add(start)
    path.add(start)

    i = 0

    while i < len(graph[start]):

        vertex = graph[start][i]

        if vertex not in visited:

            Bool = dfs_graph_c_D_T(vertex, graph, visited, path, sort)

            if Bool == True:
                return True

        elif vertex in path:

            return True

        i += 1

    path.remove(start)
    sort.append(start)

    return False


# this is BigO(e + v) in Time and BigO(v) in space


def khan_algo(graph):
    indegree = dict()

    for i in graph:
        indegree[i] = 0

    for i in graph:

        for j in graph[i]:
            indegree[j] += 1

    queue = deque()

    for i in indegree:

        if indegree[i] == 0:
            queue.append(i)

    sort = list()

    while queue:

        vertex = queue.popleft()

        sort.append(vertex)

        for i in graph[vertex]:

            indegree[i] -= 1

            if indegree[i] == 0:
                queue.append(i)

    if len(sort) == len(graph):

        return sort

    else:

        return None


# this is BigO(e + v) in Time and BigO(v) in space
def birate_graph(graph):
    visited = set()

    colour = dict()

    for i in graph:

        if i not in visited:

            colour[i] = 0

            Bool = bfs_biba(graph, i, visited, colour)

            if Bool == False:
                return False

    return True


def bfs_biba(graph, start, visited, colour):
    queue = deque()

    visited.add(start)

    queue.append(start)

    while queue:

        vertex = queue.popleft()

        for i in graph[vertex]:

            if i not in visited:

                visited.add(i)

                col = colour[vertex]

                colour[i] = col ^ 1  # Xor operation with one ,give you opposite colour

                queue.append(i)

            else:

                if colour[vertex] == colour[i]:
                    return False

    return True


# this is BigO(e + v) in Time and BigO(v) in space


def shortest_path(graph, source, element):
    visited = set()

    distance = dict()

    parent = dict()

    queue = deque()

    visited.add(source)

    queue.append(source)

    distance[source] = 0

    while queue:

        vertex = queue.popleft()

        for i in graph[vertex]:

            if i not in visited:
                visited.add(i)

                queue.append(i)

                distance[i] = distance[vertex] + 1

                parent[i] = vertex

    path = list()

    if element not in visited:
        return (-1)

    i = element

    while True:

        p = parent[i]

        path.append(p)

        if p == source:
            break

        i = p

    path.reverse()

    path.append(element)

    return (distance[element], path)


# this is BigO(e + v) in Time and BigO(v) in space


# graph = {
#     0: [(1, 4), (2, 2)],
#     1: [(0, 4), (3, 1)],
#     2: [(0, 2), (3, 3)],
#     3: [(1, 1), (2, 3)]
# }


import heapq


def dijstra(graph, source, target):
    heap = list()

    parent = dict()

    removed = set()

    distance = dict()

    heapq.heappush(heap, (0, source, None))

    while heap:

        ver_dist, vertex, _parent = heapq.heappop(heap)

        if vertex in removed:
            continue

        removed.add(vertex)

        distance[vertex] = ver_dist

        parent[vertex] = _parent

        for nei, nei_dist in graph[vertex]:
            total = ver_dist + nei_dist

            heapq.heappush(heap, (total, nei, vertex))

    if target not in removed:
        return (-1, [])

    path = list()

    i = target

    while True:

        p = parent[i]

        path.append(p)

        i = p

        if p == source:
            break

    path.reverse()

    path.append(target)

    return (distance[target], path)


# this is BigO((V+e)logv) in Time and BigO(V+E) IN SPACE   ,this is for simple graph


def prims_algo(graph):
    visited = set()

    heap = list()

    total_weight = 0

    a = next(iter(graph))

    answer = list()

    heapq.heappush(heap, (0, a, None))

    while heap:

        edge = heapq.heappop(heap)

        distance, vertex, parent = edge

        if vertex in visited:
            continue

        visited.add(vertex)

        total_weight += distance

        answer.append((edge))

        for i, dis in graph[vertex]:
            heapq.heappush(heap, (dis, i, vertex))

    if len(graph) > len(visited):
        return (None, [])

    return (total_weight, answer)


# this solution is (elogv) in Time and O(v+e) in space , for simple graph

class dsu:

    def __init__(self, graph):

        self.parent_info = dict()
        self.count_info = dict()

        for i in graph:
            self.parent_info[i] = i
            self.count_info[i] = 1

    def find(self, vertex):

        if self.parent_info[vertex] == vertex:

            return vertex

        else:

            p = self.parent_info[vertex]

            v = self.find(p)

            self.parent_info[vertex] = v  # this is path compression

            return v

    def check(self, edge):

        dis, v1, v2 = edge

        p1 = self.find(v1)
        p2 = self.find(v2)
        if p1 == p2:

            return True

        else:

            if self.count_info[p1] >= self.count_info[p2]:  # this is merging by size

                self.parent_info[p2] = p1  # updating root node
                self.count_info[p1] += self.count_info[p2]  # updating count

            else:

                self.parent_info[p1] = p2
                self.count_info[p2] += self.count_info[p1]

            return False

    # height only increse if tree of same size ,and that only by one , so max height can be logv , if is number of elemnts
    # so finding root of a vertex max takes logv time , and with path compresion almost constant time


def krushal_algo(graph):
    edges = list()

    answer = list()

    for vertex in graph:

        for i in graph[vertex]:
            pair, distance = i

            edges.append((distance, vertex, pair))

    edges.sort()

    ds = dsu(graph)

    total = 0

    for edge in edges:

        if not ds.check(edge):
            dis, v1, v2 = edge

            answer.append(edge)

            total += dis

    return (total, answer)


# this is BigO(eloge) in time and BigO(e) in space , e for edges


def bellam_ford(graph, source, target):
    distances = dict()

    iterations = len(graph)

    parent = dict()

    for vertex in graph:
        distances[vertex] = None

    distances[source] = 0

    parent[source] = source

    while iterations:

        for vertex in graph:

            if distances[vertex] != None:

                for edge, distance in graph[vertex]:

                    if distances[edge] == None or distances[edge] > distances[vertex] + distance:

                        distances[edge] = distances[vertex] + distance

                        parent[edge] = vertex

                        if iterations == 1:
                            return (None, [])
        iterations -= 1

    if target not in parent:
        return (None, [])

    i = target

    path = list()

    while True:

        path.append(i)

        if parent[i] == i:
            break

        i = parent[i]

    path.reverse()

    return (distances[target], path)


# this is BigO((VE) IN Time and BigO(V) in space ,V vertex and E edges


def dfs_graph_scc(start, graph, visited, stack, reverse_graph, private_visited):
    visited.add(start)

    if private_visited != None:
        private_visited.append(start)

    i = 0

    while i < len(graph[start]):

        vertex = graph[start][i]

        if reverse_graph != None:
            reverse_graph[vertex].append(start)

        if vertex not in visited:
            dfs_graph_scc(vertex, graph, visited, stack, reverse_graph, private_visited)

        i += 1

    if stack != None:
        stack.append(start)

    return


def SCC_kosaraju(graph):
    visited = set()
    reverse_graph = dict()

    for i in graph:
        reverse_graph[i] = list()

    stack = list()

    for i in graph:

        if i not in visited:
            dfs_graph_scc(i, graph, visited, stack, reverse_graph, None)

    parent_v = set()

    count = 0

    answer = list()

    while stack:

        i = stack.pop()

        if i not in parent_v:
            private_visited = list()

            dfs_graph_scc(i, reverse_graph, parent_v, None, None, private_visited)

            count += 1

            answer.append(private_visited)

    return (count, answer)

# time is BigO(V+E) ,  space is BigO(V+e)