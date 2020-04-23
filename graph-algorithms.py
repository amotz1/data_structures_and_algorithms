import hashtable


import hashtable


# partial implementation of a directed graph
# the graph supports vertices and edges

class Graph:
    def __init__(self) -> object:
        self.label2vertex_or_edge = hashtable.Hashtable()

    def create_vertex(self, label):
        vertex = Vertex(label)
        self.label2vertex_or_edge.put(label, vertex)

    def create_edge(self, src, dest, weight):
        edge = Edge(src, dest, weight)
        self.label2vertex_or_edge.put(edge.label, edge)
        src = self.label2vertex_or_edge.get(src.label)
        dest = self.label2vertex_or_edge.get(dest.label)
        src.add_edge(edge)
        dest.add_edge(edge)

    def get_vertex(self, label):
        vertex = self.label2vertex_or_edge.get(label)
        return vertex

    def get_edge(self, src, dest):
        edge_label = '{}-{}'.format(src.label, dest.label)
        edge = self.label2vertex_or_edge.get(edge_label)
        return edge

    # def traverse(self):
    #
    # def edges_weights_sum(self):
    #
    # def get_neighbors(self):
    # def most_connected_path(self):
    #
    # def least_connected_path(self):


class Vertex:
    def __init__(self, label):
        self.label = label
        self.edges = []

    def get_label(self):
        return self.label

    def add_edge(self, edge):
        self.edges.append(edge)


class Edge:
    def __init__(self, src, dest, weight):
        self.label = '{}-{}'.format(src.label, dest.label)
        self.src = src
        self.dest = dest
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
    nerve = brain_network.get_edge(brain_stem, thalamus)
    assert nerve.src == brain_stem
    assert nerve.dest == thalamus
    brain_network.create_edge(brain_stem, amygdala, 5)
    nerve = brain_network.get_edge(brain_stem, amygdala)
    assert nerve.src == brain_stem
    assert nerve.dest == amygdala
    brain_network.create_edge(brain_stem, hypocampus, 5)
    nerve = brain_network.get_edge(brain_stem, hypocampus)
    assert nerve.src == brain_stem
    assert nerve.dest == hypocampus
    brain_network.create_edge(thalamus, frontal_lobe, 5)
    nerve = brain_network.get_edge(thalamus, frontal_lobe)
    assert nerve.src == thalamus
    assert nerve.dest == frontal_lobe
    brain_network.create_edge(amygdala, frontal_lobe, 8)
    nerve = brain_network.get_edge(amygdala, frontal_lobe)
    assert nerve.src == amygdala
    assert nerve.dest == frontal_lobe
    brain_network.create_edge(hypocampus, frontal_lobe, 10)
    nerve = brain_network.get_edge(hypocampus, frontal_lobe)
    assert nerve.src == hypocampus
    assert nerve.dest == frontal_lobe
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

