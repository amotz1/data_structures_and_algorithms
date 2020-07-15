import hashtable
import stack
import queue
import mergesort


#  implementation of a dfs, recursive dfs and bfs on an undirected graph


class Graph:
    def __init__(self):
        self.label2vertex = hashtable.Hashtable()

    def create_vertex(self, label):
        vertex = Vertex(label)
        self.label2vertex.put(label, vertex)
        return vertex

    def create_edge(self, vertex_obj_1, vertex_obj_2, weight):
        # checking that both two argument vertices are Vertex instances that are present in the graph
        assert hasattr(vertex_obj_1, 'label') is True, 'either one or two of the objects you try to connect ' \
                                                       'are not vertices'
        assert hasattr(vertex_obj_2, 'label') is True, ' either one or two of the objects you try to connect ' \
                                                       'are not vertices'
        assert self.label2vertex.get(vertex_obj_1.label) == vertex_obj_1, 'either one or two of the vertices you try ' \
                                                                          'to connect are not in the graph'
        assert self.label2vertex.get(vertex_obj_2.label) == vertex_obj_2, 'either one or two of the vertices ' \
                                                                          'you try to connect are not in the graph'
        edge = Edge(vertex_obj_1, vertex_obj_2, weight)
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


class Edge:
    def __init__(self, vertex_obj_1, vertex_obj_2, weight):
        self.vertex_obj_1 = vertex_obj_1
        self.vertex_obj_2 = vertex_obj_2
        self.weight = weight


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
        neighbor_list = vertex.get_neighbors().reverse()
        for neighbor in neighbor_list:
            if seen.get(neighbor.label) is None:
                Algorithms._recursive_dfs(neighbor, vertices_list, seen)

    @ staticmethod
    def recursive_dfs(vertex):
        seen = hashtable.Hashtable()
        vertices_list = []
        Algorithms._recursive_dfs(vertex, vertices_list, seen)
        return vertices_list

    @staticmethod
    def bfs(root):
        vertices_list = []
        seen = hashtable.Hashtable()
        qu = queue.Queue()
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

# def create_test_graph_1():
#     isolated_cities = Graph()
#     for vertex in ['jerusalem', 'haifa']:
#         isolated_cities.create_vertex(vertex)




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

    graph_algorithms = Algorithms()
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

    # TODO making some more graph tests
    #  (2 isolated vertices with no neighbors and 2 isolated subgraphs with two neighbors)



#
#
# # assert brain_network.edges_weights_sum('amygdala') == 8
# # assert brain_network.edges_weights_sum('frontal_lobe') == 0
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
