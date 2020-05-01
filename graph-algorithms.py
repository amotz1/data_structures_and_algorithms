import hashtable

import hashtable


# partial implementation of a directed graph
# the graph supports vertices and edges

class Graph:
    def __init__(self) -> object:
        self.label2vertex = hashtable.Hashtable()

    def create_vertex(self, label):
        vertex = Vertex(label)
        self.label2vertex.put(label, vertex)
        return vertex

    def create_edge(self, vertex_obj_1, vertex_obj_2, weight):
        # checking that both two argument vertices are present in the graph
        vertices_arguments_in_graph = 0
        for i in self.label2vertex:
            if i.value == vertex_obj_1 or i.value == vertex_obj_2:
                vertices_arguments_in_graph += 1
        assert vertices_arguments_in_graph == 2, "one or both of the vertices that you specified are not in the graph"
        edge = Edge(vertex_obj_1, vertex_obj_2, weight)
        vertex_obj_1 = self.label2vertex.get(vertex_obj_1.label)
        vertex_obj_2 = self.label2vertex.get(vertex_obj_2.label)
        vertex_obj_1.add_edge(edge)
        vertex_obj_2.add_edge(edge)
        vertex_obj_1.add_vertex_neighbor(edge.vertex_obj_2)
        vertex_obj_2.add_vertex_neighbor(edge.vertex_obj_1)
        return edge

    def get_vertex(self, label):
        vertex = self.label2vertex.get(label)
        return vertex

    # def traverse(self):
    #
    # def edges_weighths_sum(self):
    #
    # def get_neighbors(self):
    # def most_connected_path(self):
    #
    # def least_connected_path(self):


class Vertex:
    def __init__(self, label):
        self.label = label
        self.edges = []
        self.neighbors = []

    @property
    def get_label(self):
        return self.label

    @property
    def get_neighbors(self):
        return self.neighbors

    def add_edge(self, edge):
        self.edges.append(edge)

    def add_vertex_neighbor(self, neighbor):
        self.neighbors.append(neighbor)


class Edge:
    def __init__(self, vertex_obj_1, vertex_obj_2, weight):
        self.vertex_obj_1 = vertex_obj_1
        self.vertex_obj_2 = vertex_obj_2
        self.weight = weight


def test_Graph():
    brain_network: Graph = Graph()
    assert brain_network.get_vertex('hillel') is None
    for vertex in ['hypocampus', 'thalamus', 'amygdala', 'frontal_lobe', 'brain_stem']:
        brain_network.create_vertex(vertex)
        brain_region = brain_network.get_vertex(vertex)
        assert brain_region.label == vertex
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
    assert frontal_lobe.get_neighbors[0].label == 'thalamus'
    assert frontal_lobe.get_neighbors[1].label == 'amygdala'
    assert frontal_lobe.get_neighbors[2].label == 'hypocampus'
    # assert brain_network.traverse() == ['brain_stem','hypocampus','amygdala','frontal_lobe']
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


test_Graph()
