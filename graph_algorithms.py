import hashtable
import stack
import queue1
import sys


#  implementation of a dfs, recursive dfs and bfs on an undirected graph
#  implementation of a shortest path algorithm
#  implementation of a shortest path brute force algorithm with bugs


class Graph:
    def __init__(self):
        self.label2vertex = hashtable.Hashtable()

    def create_vertex(self, label):
        vertex = Vertex(label)
        self.label2vertex.put(label, vertex)
        return vertex

    def create_edge(self, vertex_1, vertex_2, length):
        # checking that both two argument vertices are Vertex instances that are present in the graph
        assert hasattr(vertex_1, 'label') is True, 'either one or two of the objects you try to connect ' \
                                                   'are not vertices'
        assert hasattr(vertex_2, 'label') is True, ' either one or two of the objects you try to connect ' \
                                                   'are not vertices'
        assert self.label2vertex.get(vertex_1.label) == vertex_1, 'either one or two of the vertices you try ' \
                                                                  'to connect are not in the graph'
        assert self.label2vertex.get(vertex_2.label) == vertex_2, 'either one or two of the vertices ' \
                                                                  'you try to connect are not in the graph'
        edge = Edge(vertex_1, vertex_2, length)
        # appending the edge and the vertices it contains
        # to a separate edges and neighbors_list lists in vertices objects
        vertex_1 = self.label2vertex.get(vertex_1.label)
        vertex_2 = self.label2vertex.get(vertex_2.label)
        vertex_1.edges.append(edge)
        vertex_2.edges.append(edge)
        vertex_1.neighbors_list.append(edge.vertex_2)
        vertex_2.neighbors_list.append(edge.vertex_1)
        return edge

    def get_vertex(self, label):
        vertex = self.label2vertex.get(label)
        return vertex


class Vertex:
    def __init__(self, label):
        self.label = label
        self.edges = []
        self.neighbors_list = []

    def get_label(self):
        return self.label

    def __str__(self):
        return self.label

    def __repr__(self):
        return self.__str__()

    def get_neighbors(self):
        # making a copy to vertex.get_neighbors() because
        # messing with this will break the graph integrity
        neighbors_list_copy = list(self.neighbors_list)
        return neighbors_list_copy

    def get_edges(self):
        edges_list_copy = list(self.edges)
        return edges_list_copy


class Edge:
    def __init__(self, vertex_1, vertex_2, length):
        self.vertex_1 = vertex_1
        self.vertex_2 = vertex_2
        self.length = length

    def get_length(self):
        return self.length

    def get_other_vertex(self, vertex):
        if self.vertex_1 == vertex:
            return self.vertex_2
        elif self.vertex_2 == vertex:
            return self.vertex_1
        else:
            assert False, 'the vertex is not an attribute of the edge'

    def __str__(self):
        return '{}-{}({})'.format(self.vertex_1, self.vertex_2, self.length)

    def __repr__(self):
        return self.__str__()


class Algorithms:
    @staticmethod
    def dfs(root):
        vertices_list = []
        seen = hashtable.Hashtable()
        st = stack.Stack()
        st.push(root)
        while not st.is_empty():
            vertex = st.pop()
            if seen.get(vertex.label) is not None:
                continue
            seen.put(vertex.label, 'dummy')
            vertices_list.append(vertex)
            for neighbor in vertex.get_neighbors():
                if seen.get(neighbor.label) is None:
                    st.push(neighbor)
        return vertices_list

    @staticmethod
    def _recursive_dfs(vertex, vertices_list, seen):
        vertices_list.append(vertex)
        seen.put(vertex.label, 'dummy')
        # reversing the neighbors_list_copy to make recursive dfs and dfs function
        # output the same vertices
        neighbor_list = vertex.get_neighbors()
        neighbor_list.reverse()
        for neighbor in neighbor_list:
            if seen.get(neighbor.label) is None:
                Algorithms._recursive_dfs(neighbor, vertices_list, seen)

    @staticmethod
    def recursive_dfs(vertex):
        seen = hashtable.Hashtable()
        vertices_list = []
        Algorithms._recursive_dfs(vertex, vertices_list, seen)
        return vertices_list

    @staticmethod
    def bfs(root):
        vertices_list = []
        seen = hashtable.Hashtable()
        qu = queue1.Queue()
        qu.push(root)
        while not qu.is_empty():
            vertex = qu.pop().value
            if seen.get(vertex.label) is not None:
                continue
            seen.put(vertex.label, 'dummy')
            vertices_list.append(vertex)
            for neighbor in vertex.get_neighbors():
                if seen.get(neighbor.label) is None:
                    qu.push(neighbor)
        return vertices_list

    @staticmethod
    def shortest_path(source, dest):

        # Path length refers to the shortest path length that the algorithm has found so far
        # from the source to a visited vertex
        vertex2path_length = {source: 0}

        # Path refers to the shortest path that the algorithm has found so far
        # from the source to a visited vertex
        vertex2path = {source: []}

        # active path end refer to the city at the end of each active path that we are developing
        active_path_ends = {source: 'dummy'}

        # stopping to search for new active paths when we don't have any active path ends anymore
        while len(active_path_ends) != 0:

            # choosing the city with the current shortest path length from the active path ends
            shortest_path_end = None
            path_ends_min = sys.maxsize
            for path_end, dummy in active_path_ends.items():
                if vertex2path_length[path_end] < path_ends_min:
                    path_ends_min = vertex2path_length[path_end]
                    shortest_path_end = path_end
            assert shortest_path_end is not None

            # TODO making path_end a sorted path_ends structure
            #  so finding the vertex with the minimum path_length could take o[1] instead of o[n]

            # after choosing the city, i start to develop from it new paths, so this city is not a path end anymore.
            del active_path_ends[shortest_path_end]

            # stopping to search for new active paths when the path length from source to dest
            # is smaller then the smallest path that we developed
            if dest in vertex2path_length and vertex2path_length[dest] < path_ends_min:
                break

            # visiting the neighboring cities and updating the current shortest path to them.
            # if the neighbor city is not the destination and i updated its current shortest path length,
            # i also add it as an end of an active path for future exploration.
            for edge in shortest_path_end.get_edges():
                neighbor = edge.get_other_vertex(shortest_path_end)
                if neighbor not in vertex2path_length:
                    vertex2path_length[neighbor] = vertex2path_length[shortest_path_end] + edge.length
                    # creating a temporary copy of vertex2path[shortest_path_end]
                    # and appending the edge to it so the original variable will not be affected
                    copy = vertex2path[shortest_path_end][:]
                    copy.append(edge)
                    vertex2path[neighbor] = copy
                    if neighbor != dest:
                        active_path_ends[neighbor] = 'dummy'
                else:
                    if vertex2path_length[shortest_path_end] + edge.length < vertex2path_length[neighbor]:
                        vertex2path_length[neighbor] = vertex2path_length[shortest_path_end] + edge.length
                        copy = vertex2path[shortest_path_end][:]
                        copy.append(edge)
                        vertex2path[neighbor] = copy
                        if neighbor != dest:
                            active_path_ends[neighbor] = 'dummy'
        return vertex2path_length[dest], vertex2path[dest]

    @staticmethod
    def compute_all_paths(source, dest):

        path_end = source
        active_path = []
        paths = []

        Algorithms._compute_all_paths(path_end, dest, active_path, paths)
        print('paths = %s' % paths)
        return paths

    @staticmethod
    def _compute_all_paths(path_end, dest, active_path, paths):

        for edge in path_end.edges:

            neighbor = edge.get_other_vertex(path_end)

            if neighbor != dest:
                path_vertices = find_path_vertices(active_path)

                if neighbor not in path_vertices:
                    next_active_path = active_path[:]  # making a copy of the current active path
                    next_active_path.append(edge)
                    Algorithms._compute_all_paths(neighbor, dest, next_active_path, paths)

            else:
                complete_path = active_path[:]
                complete_path.append(edge)
                paths.append(complete_path)


def find_path_vertices(edges_list):

    path_vertices = []

    if edges_list == []:
        return []

    source = edges_list[0].vertex_1
    path_vertices.append(source)

    other_vertex = source
    for edge in edges_list:
        other_vertex = edge.get_other_vertex(other_vertex)
        path_vertices.append(other_vertex)

    return path_vertices
