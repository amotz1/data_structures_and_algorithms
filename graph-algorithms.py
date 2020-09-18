import hashtable
import stack
import queue1
import mergesort
import sys


#  implementation of a dfs, recursive dfs and bfs on an undirected graph
#  implementation of a shortest path algorithm


class Graph:
    def __init__(self):
        self.label2vertex = hashtable.Hashtable()

    def create_vertex(self, label):
        vertex = Vertex(label)
        self.label2vertex.put(label, vertex)
        return vertex

    def create_edge(self, vertex_obj_1, vertex_obj_2, length):
        # checking that both two argument vertices are Vertex instances that are present in the graph
        assert hasattr(vertex_obj_1, 'label') is True, 'either one or two of the objects you try to connect ' \
                                                       'are not vertices'
        assert hasattr(vertex_obj_2, 'label') is True, ' either one or two of the objects you try to connect ' \
                                                       'are not vertices'
        assert self.label2vertex.get(vertex_obj_1.label) == vertex_obj_1, 'either one or two of the vertices you try ' \
                                                                          'to connect are not in the graph'
        assert self.label2vertex.get(vertex_obj_2.label) == vertex_obj_2, 'either one or two of the vertices ' \
                                                                          'you try to connect are not in the graph'
        edge = Edge(vertex_obj_1, vertex_obj_2, length)
        # appending the edge and the vertices it contains
        # to a separate edges and neighbors_list lists in vertices objects
        vertex_obj_1 = self.label2vertex.get(vertex_obj_1.label)
        vertex_obj_2 = self.label2vertex.get(vertex_obj_2.label)
        vertex_obj_1.edges.append(edge)
        vertex_obj_2.edges.append(edge)
        vertex_obj_1.neighbors_list.append(edge.vertex_obj_2)
        vertex_obj_2.neighbors_list.append(edge.vertex_obj_1)
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

    def get_neighbors(self):
        # making a copy to vertex.get_neighbors() because
        # messing with this will break the graph integrity
        neighbors_list_copy = list(self.neighbors_list)
        return neighbors_list_copy

    def get_edges(self):
        return self.edges


class Edge:
    def __init__(self, vertex_obj_1, vertex_obj_2, length):
        self.vertex_obj_1 = vertex_obj_1
        self.vertex_obj_2 = vertex_obj_2
        self.length = length

    def get_length(self):
        return self.length

    def get_other_vertex(self, vertex):
        if self.vertex_obj_1 == vertex:
            return self.vertex_obj_2
        else:
            return self.vertex_obj_1


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

            # stopping to search for new active paths when the path length from source to dest
            # is smaller then the smallest path that we developed
            if dest in vertex2path_length and vertex2path_length[dest] < path_ends_min:
                break

            # after choosing the city, i start to develop from it new paths, so this city is not a path end anymore.
            del active_path_ends[shortest_path_end]

            # visiting the neighboring cities and updating the current shortest path to them.
            # if the neighbor city is not the destination and i updated its current shortest path length,
            # i also add it as an end of an active path for future exploration.
            for edge in shortest_path_end.get_edges():
                neighbor = edge.get_other_vertex(shortest_path_end)
                if neighbor not in vertex2path_length:
                    vertex2path_length[neighbor] = vertex2path_length[shortest_path_end] + edge.length
                    if neighbor != dest:
                        active_path_ends[neighbor] = 'dummy'
                else:
                    if vertex2path_length[shortest_path_end] + edge.length < vertex2path_length[neighbor]:
                        vertex2path_length[neighbor] = vertex2path_length[shortest_path_end] + edge.length
                        if neighbor != dest:
                            active_path_ends[neighbor] = 'dummy'
        return vertex2path_length[dest]


def create_test_graph():
    brain_network = Graph()
    for vertex in ['hypocampus', 'thalamus', 'amygdala', 'frontal_lobe', 'brain_stem']:
        brain_network.create_vertex(vertex)
    brain_stem = brain_network.get_vertex('brain_stem')
    thalamus = brain_network.get_vertex('thalamus')
    amygdala = brain_network.get_vertex('amygdala')
    frontal_lobe = brain_network.get_vertex('frontal_lobe')
    hypocampus = brain_network.get_vertex('hypocampus')
    brain_network.create_edge(brain_stem, thalamus, 3)
    brain_network.create_edge(brain_stem, amygdala, 5)
    brain_network.create_edge(brain_stem, hypocampus, 5)
    brain_network.create_edge(thalamus, frontal_lobe, 5)
    brain_network.create_edge(amygdala, frontal_lobe, 8)
    brain_network.create_edge(hypocampus, frontal_lobe, 10)
    return brain_network


def create_test_graph_1():
    isolated_cities = Graph()
    for city in ['jerusalem', 'haifa']:
        isolated_cities.create_vertex(city)
    return isolated_cities


def create_test_graph_2():
    two_pairs_of_cities = Graph()
    for city in ['jerusalem', 'haifa', 'rishon', 'hulon']:
        two_pairs_of_cities.create_vertex(city)
    hulon = two_pairs_of_cities.get_vertex('hulon')
    rishon = two_pairs_of_cities.get_vertex('rishon')
    haifa = two_pairs_of_cities.get_vertex('haifa')
    jerusalem = two_pairs_of_cities.get_vertex('jerusalem')
    two_pairs_of_cities.create_edge(haifa, rishon, 3)
    two_pairs_of_cities.create_edge(jerusalem, hulon, 5)
    return two_pairs_of_cities


def create_test_cities():
    israel_cities = Graph()
    hulon = israel_cities.create_vertex('hulon')
    rishon = israel_cities.create_vertex('rishon')
    haifa = israel_cities.create_vertex('haifa')
    beer_sheva = israel_cities.create_vertex('beer_sheva')
    naharia = israel_cities.create_vertex('naharia')
    eilat = israel_cities.create_vertex('eilat')
    israel_cities.create_edge(haifa, hulon, 25)
    israel_cities.create_edge(haifa, eilat, 100)
    israel_cities.create_edge(haifa, rishon, 40)
    israel_cities.create_edge(hulon, rishon, 50)
    israel_cities.create_edge(hulon, naharia, 60)
    israel_cities.create_edge(rishon, beer_sheva, 20)
    israel_cities.create_edge(naharia, eilat, 10)
    israel_cities.create_edge(naharia, beer_sheva, 20)
    israel_cities.create_edge(beer_sheva, eilat, 90)
    return israel_cities


def create_test_cities_1():
    israel_cities = Graph()
    haifa = israel_cities.create_vertex('haifa')
    petach_tikva = israel_cities.create_vertex('petach_tikva')
    rishon = israel_cities.create_vertex('rishon')
    eilat = israel_cities.create_vertex('eilat')
    israel_cities.create_edge(haifa, eilat, 10)
    israel_cities.create_edge(haifa, petach_tikva, 2)
    israel_cities.create_edge(haifa, rishon, 12)
    israel_cities.create_edge(petach_tikva, eilat, 1)
    israel_cities.create_edge(rishon, eilat, 30)
    return israel_cities


def test_Graph():
    brain_network = create_test_graph()
    # vertex that is not in the graph
    assert brain_network.get_vertex('hillel') is None
    for vertex in ['hypocampus', 'thalamus', 'amygdala', 'frontal_lobe', 'brain_stem']:
        # every vertex  that we created is in the graph
        assert brain_network.get_vertex(vertex).label == vertex
    frontal_lobe = brain_network.get_vertex('frontal_lobe')
    thalamus = brain_network.get_vertex('thalamus')
    amygdala = brain_network.get_vertex('amygdala')
    hypocampus = brain_network.get_vertex('hypocampus')
    brain_stem = brain_network.get_vertex('brain_stem')
    # vertex contain its neighbors
    assert frontal_lobe.neighbors_list[0].label == 'thalamus'
    assert frontal_lobe.neighbors_list[1].label == 'amygdala'
    assert frontal_lobe.neighbors_list[2].label == 'hypocampus'

    dfs_vertices = Algorithms.dfs(thalamus)
    rec_dfs_vertices = Algorithms.recursive_dfs(thalamus)
    # dfs and recursive dfs output with root node thalamus
    assert list(map(lambda x: x.label, dfs_vertices)) == ['thalamus', 'frontal_lobe', 'hypocampus', 'brain_stem',
                                                          'amygdala']

    # checking that the output of dfs and recursive dfs are the same
    assert rec_dfs_vertices == dfs_vertices

    # checking dfs and recursive dfs for other nodes
    dfs_vertices = Algorithms.dfs(frontal_lobe)
    rec_dfs_vertices = Algorithms.recursive_dfs(frontal_lobe)
    assert [vertex.label for vertex in dfs_vertices] == ['frontal_lobe', 'hypocampus', 'brain_stem',
                                                         'amygdala', 'thalamus']
    assert rec_dfs_vertices == dfs_vertices
    dfs_vertices = Algorithms.dfs(amygdala)
    rec_dfs_vertices = Algorithms.recursive_dfs(amygdala)
    assert list(map(lambda x: x.label, dfs_vertices)) == ['amygdala', 'frontal_lobe', 'hypocampus', 'brain_stem',
                                                          'thalamus']
    assert dfs_vertices == rec_dfs_vertices
    dfs_vertices = Algorithms.dfs(brain_stem)
    rec_dfs_vertices = Algorithms.recursive_dfs(brain_stem)
    assert [vertex.label for vertex in dfs_vertices] == ['brain_stem', 'hypocampus', 'frontal_lobe', 'amygdala',
                                                         'thalamus']
    assert (dfs_vertices == rec_dfs_vertices)
    dfs_vertices = Algorithms.dfs(hypocampus)
    rec_dfs_vertices = Algorithms.recursive_dfs(hypocampus)
    assert list(map(lambda x: x.label, dfs_vertices)) == ['hypocampus', 'frontal_lobe', 'amygdala',
                                                          'brain_stem', 'thalamus']
    assert rec_dfs_vertices == dfs_vertices

    # bfs output with root node thalamus
    bfs_vertices = Algorithms.bfs(thalamus)
    assert ([vertex.label for vertex in bfs_vertices] == ['thalamus', 'brain_stem', 'frontal_lobe',
                                                          'amygdala', 'hypocampus'])

    # sorting bfs output is equivalent to sorting dfs output (using our good old mergesort :))
    assert (mergesort.sort([vertex.label for vertex in bfs_vertices]) == mergesort.sort([vertex.label for vertex
                                                                                         in dfs_vertices]))
    isolated_cities = create_test_graph_1()
    haifa = isolated_cities.get_vertex('haifa')
    jerusalem = isolated_cities.get_vertex('jerusalem')
    for city in [haifa, jerusalem]:
        dfs_vertices = Algorithms.dfs(city)
        rec_dfs_vertices = Algorithms.recursive_dfs(city)
        bfs_vertices = Algorithms.bfs(city)
        assert dfs_vertices == bfs_vertices
        assert rec_dfs_vertices == dfs_vertices

    two_pairs_of_cities = create_test_graph_2()
    haifa = two_pairs_of_cities.get_vertex('haifa')
    jerusalem = two_pairs_of_cities.get_vertex('jerusalem')
    dfs_vertices_haifa = Algorithms.dfs(haifa)
    dfs_vertices_jerusalem = Algorithms.dfs(jerusalem)
    assert list(map(lambda x: x.label, dfs_vertices_haifa)) == ['haifa', 'rishon']
    assert [vertex.label for vertex in dfs_vertices_jerusalem] == ['jerusalem', 'hulon']
    for city in [haifa, jerusalem]:
        dfs_vertices = Algorithms.dfs(city)
        rec_dfs_vertices = Algorithms.recursive_dfs(city)
        bfs_vertices = Algorithms.bfs(city)
        assert dfs_vertices == bfs_vertices
        assert rec_dfs_vertices == dfs_vertices
    israel_cities = create_test_cities()
    haifa = israel_cities.get_vertex('haifa')
    rishon = israel_cities.get_vertex('rishon')
    eilat = israel_cities.get_vertex('eilat')
    shortest_path = Algorithms.shortest_path(haifa, haifa)
    assert shortest_path == 0
    shortest_path = Algorithms.shortest_path(haifa, rishon)
    assert shortest_path == 40
    shortest_path = Algorithms.shortest_path(rishon, haifa)
    assert shortest_path == 40
    shortest_path = Algorithms.shortest_path(haifa, eilat)
    assert shortest_path == 90
    israel_cities = create_test_cities_1()
    haifa = israel_cities.get_vertex('haifa')
    eilat = israel_cities.get_vertex('eilat')
    shortest_path = Algorithms.shortest_path(haifa, eilat)
    assert shortest_path == 3

    # TODO finding away to import mergsort in a way that my program will not run mergesort.py when i run it
    # TODO changing the edges to be uni-directional


#
#
# # assert brain_network.edges_weights_sum('amygdala') == 8
# # assert brain_network.edges_weights_sum('frontal_lobe') ==
# # assert brain_network.edges_weights_sum('hypocampus') == 10
# # assert brain_network.edges_weights_sum('thalamus') == 5
# # assert brain_network. edges_weights_sum('brain_stem') == 13
# # neighbors_list = brain_network.get_neighbors('brain_stem')
# # assert neighbors_list[0].get_label() == 'hypocampus'
# # assert neighbors_list[1].get_label() == 'thalamus'
# # assert neighbors_list[2].get_label() == 'amygdala'
# # assert brain_network.most_connected_path('brain_stem','frontal_lobe') == ['brain_stem' , 'hypocampus', 'frontal_lobe', 15]
# # assert brain_network.least_connected_path('brain_stem','frontal_lobe') == ['brain_stem', 'thalamus', 'frontal_lobe', 8]
# #
#
test_Graph()
