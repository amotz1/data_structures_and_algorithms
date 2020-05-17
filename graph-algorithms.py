import hashtable

import hashtable


# implementation of an undirected graph, the graph supports vertices and edges
#  added a partial implementation of a stack class but no algorithms yet

class Graph:
    def __init__(self):
        self.label2vertex = hashtable.Hashtable()

    def create_vertex(self, label):
        vertex = Vertex(label)
        self.label2vertex.put(label, vertex)
        return vertex

    def create_edge(self, vertex_obj_1, vertex_obj_2, weight):
        # checking that both two argument vertices are present in the graph
        assert hasattr(vertex_obj_1, 'label') is True, 'either one or two of the objects you try to connect ' \
                                                       'are not vertices'
        assert hasattr(vertex_obj_2, 'label') is True, ' either one or two of the objects you try to connect ' \
                                                       'are not vertices'
        assert self.label2vertex.get(vertex_obj_1.label) == vertex_obj_1, 'either one or two of the vertices you try ' \
                                                                          'to connect is not in the graph'
        assert self.label2vertex.get(vertex_obj_2.label) == vertex_obj_2, 'either one or two of the vertices ' \
                                                                          'you try to connect is not in the graph'
        edge = Edge(vertex_obj_1, vertex_obj_2, weight)
        vertex_obj_1 = self.label2vertex.get(vertex_obj_1.label)
        vertex_obj_2 = self.label2vertex.get(vertex_obj_2.label)
        vertex_obj_1.edges.append(edge)
        vertex_obj_2.edges.append(edge)
        vertex_obj_1.neighbors.append(edge.vertex_obj_2)
        vertex_obj_2.neighbors.append(edge.vertex_obj_1)
        return edge

    def get_vertex(self, label):
        vertex = self.label2vertex.get(label)
        return vertex


class Vertex:
    def __init__(self, label):
        self.label = label
        self.edges = []
        self.neighbors = []

    def get_label(self):
        return self.label

    def get_neighbors(self):
        return self.neighbors


class Edge:
    def __init__(self, vertex_obj_1, vertex_obj_2, weight):
        self.vertex_obj_1 = vertex_obj_1
        self.vertex_obj_2 = vertex_obj_2
        self.weight = weight


class Stack:

    def __init__(self, array_size):
        self.array = [None] * array_size
        self.top = -1

    def push(self, vertex_obj):
        assert self.top != len(self.array) - 1, "the stack is full of elements"
        self.top = self.top + 1
        self.array[self.top] = vertex_obj

    def pop(self):
        assert self.top != -1, "the stack is empty"
        vertex_obj = self.array[self.top]
        self.array[self.top] = None
        self.top = self.top - 1
        return vertex_obj


# TODO a stack that dynamically change size

def test_Graph():
    brain_network = Graph()
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
    assert frontal_lobe.neighbors[0].label == 'thalamus'
    assert frontal_lobe.neighbors[1].label == 'amygdala'
    assert frontal_lobe.neighbors[2].label == 'hypocampus'
    STACK_SIZE = 1000
    stack = Stack(STACK_SIZE)
    for vertex in [brain_stem, thalamus, amygdala, hypocampus, frontal_lobe]:
        stack.push(vertex)
    for vertex in [frontal_lobe, hypocampus, amygdala, thalamus, brain_stem]:
        vertex_obj = stack.pop()
        assert vertex_obj == vertex
    # graph_algorithms = Algorithms()
    # assert graph_algorithms.dfs(brain_network, thalamus) == ['thalamus', 'brain_stem', 'hypocampus',
    #                                                          'frontal_lobe', 'amygdala']
    # assert graph_algorithms.bfs(brain_network, thalamus) == ['thalamus', 'brain_stem', 'fronta_lobe',
    #                                                          'amygdala', 'hypocampus']

    # TODO dfs algorithm


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
#

test_Graph()
