import hashtable
import stack
import queue


# implementation of an undirected graph, the graph supports vertices and edges
#  added a partial implementation of a stack and queue class and an algorithm class with
#  partial implementation of a dfs recursive dfs and bfs methods


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
        return self.neighbors_list


class Edge:
    def __init__(self, vertex_obj_1, vertex_obj_2, weight):
        self.vertex_obj_1 = vertex_obj_1
        self.vertex_obj_2 = vertex_obj_2
        self.weight = weight


class Algorithms:

    def dfs(self, graph, vertex_label):
        vertex = graph.get_vertex(vertex_label)
        vertices_list = []
        seen = hashtable.Hashtable()
        st = stack.Stack()
        st.push(vertex)
        while not st.is_empty():
            vertex = st.pop()
            vertices_list.append(vertex)
            # TODO replacing vertex object in seen hashtable with dummy variable
            seen.put(vertex.label, vertex)
            neighbors_list = vertex.get_neighbors()
            for vertex in neighbors_list:
                if seen.get(vertex.label) is not vertex:
                    st.push(vertex)
        return vertices_list

    def recursive_dfs(self, graph, vertex_label):
        seen = hashtable.Hashtable()
        vertices_list = []
        self._recursive_dfs(graph, vertex_label, vertices_list, seen)
        return vertices_list

    def _recursive_dfs(self, graph, vertex_label, vertices_list, seen):
        vertex = graph.get_vertex(vertex_label)
        vertices_list.append(vertex)
        seen.put(vertex.label, vertex)
        neighbors_list = vertex.get_neighbors()
        for vertex in neighbors_list:
            if seen.get(vertex.label) is not vertex:
                self._recursive_dfs(graph, vertex.label, vertices_list, seen)

    def bfs(self, graph, vertex_label):
        vertex = graph.get_vertex(vertex_label)
        vertices_list = []
        seen = hashtable.Hashtable()
        qu = queue.Queue()
        qu.push(vertex)
        while not qu.is_empty():
            vertex = qu.pop().value
            vertices_list.append(vertex)
            seen.put(vertex.label, vertex)
            neighbors_list = vertex.get_neighbors()
            for vertex in neighbors_list:
                if seen.get(vertex.label) is not vertex:
                    qu.push(vertex)
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


def test_Graph():
    brain_network = create_test_graph()
    # vertex that is not in the graph
    assert brain_network.get_vertex('hillel') is None
    for vertex in ['hypocampus', 'thalamus', 'amygdala', 'frontal_lobe', 'brain_stem']:
        # every vertex  that we created is in the graph
        assert brain_network.get_vertex(vertex).label == vertex
    frontal_lobe = brain_network.get_vertex('frontal_lobe')

    # vertex contain its neighbors
    assert frontal_lobe.neighbors_list[0].label == 'thalamus'
    assert frontal_lobe.neighbors_list[1].label == 'amygdala'
    assert frontal_lobe.neighbors_list[2].label == 'hypocampus'
    graph_algorithms = Algorithms()
    graph_algorithms.dfs(brain_network, 'thalamus')
    vertices_list = graph_algorithms.dfs(brain_network, 'thalamus')

    # dfs output with root node thalamus
    assert vertices_list[0].label == 'thalamus'
    assert vertices_list[1].label == 'frontal_lobe'
    assert vertices_list[2].label == 'hypocampus'
    assert vertices_list[3].label == 'brain_stem'
    assert vertices_list[4].label == 'amygdala'
    assert not vertices_list[5].label

    graph_algorithms.recursive_dfs(brain_network, 'thalamus')
    vertices_list = graph_algorithms.recursive_dfs(brain_network, 'thalamus')
    # dfs output with root node thalamus
    graph_algorithms.recursive_dfs(brain_network, 'thalamus')
    assert vertices_list[0].label == 'thalamus'
    assert vertices_list[1].label == 'brain_stem'
    assert vertices_list[2].label == 'amygdala'
    assert vertices_list[3].label == 'frontal_lobe'
    assert vertices_list[4].label == 'hypocampus'

    # bfs output with root node thalamus
    # vertices_list = graph_algorithms.bfs(brain_network, 'thalamus')
    # assert vertices_list[0].label == 'thalamus'
    # assert vertices_list[1].label == 'brain_stem'
    # assert vertices_list[2].label == 'frontal_lobe'
    # assert vertices_list[3].label == 'amygdala'
    # assert vertices_list[4].label == 'hypocampus'

    # TODO: solving the problem with duplicates in queue and stack
    # TODO change all occurrences of vertex label in my functions for vertex objects



# assert brain_network.edges_weights_sum('amygdala') == 8
# assert brain_network.edges_weights_sum('frontal_lobe') == 0
# assert brain_network.edges_weights_sum('hypocampus') == 10
# assert brain_network.edges_weights_sum('thalamus') == 5
# assert brain_network. edges_weights_sum('brain_stem') == 13
# neighbors_list = brain_network.get_neighbors('brain_stem')
# assert neighbors_list[0].get_label() == 'hypocampus'
# assert neighbors_list[1].get_label() == 'thalamus'
# assert neighbors_list[2].get_label() == 'amygdala'
# assert brain_network.most_connected_path('brain_stem','frontal_lobe') == ['brain_stem' , 'hypocampus', 'frontal_lobe', 15]
# assert brain_network.least_connected_path('brain_stem','frontal_lobe') == ['brain_stem', 'thalamus', 'frontal_lobe', 8]
#

test_Graph()
