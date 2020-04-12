import linked_list


# partial graph implementation
# the graph supports vertices that have labels but not edges
class Graph:
    def __init__(self):
        self.list = []

    def add_vertex(self, label):
        vertex = Vertex(label)
        self.list.append(vertex)

    def find_vertex(self, label):
        for i in self.list:
            if i.get_label() == label:
                return i
        return None

    # def add_edge(self, src, dest):
    #
    # def traverse(self):
    #
    # def edges_weights_sum(self):
    #
    # def get_neighbors(self):
    # A
    # def most_connected_path(self):
    #
    # def least_connected_path(self):


class Vertex:
    def __init__(self, label):
        self.label = label

    def get_label(self):
        return self.label


# class Edge:
#     def __init__(self):


def test_Graph():
    brain_network = Graph()
    brain_network.add_vertex('hypocampus')
    assert brain_network.find_vertex('hillel') is None
    brain_region = brain_network.find_vertex('hypocampus')
    assert brain_region.label == 'hypocampus'
    brain_network.add_vertex('thalamus')
    brain_region = brain_network.find_vertex('thalamus')
    assert brain_region.label == 'thalamus'
    brain_network.add_vertex('amigdala')
    brain_region = brain_network.find_vertex('amigdala')
    assert brain_region.label == 'amigdala'
    brain_network.add_vertex('frontal_lobe')
    brain_region = brain_network.find_vertex('frontal_lobe')
    assert brain_region.label == 'frontal_lobe'
    brain_network.add_vertex('brain_stem')
    brain_region = brain_network.find_vertex('brain_stem')
    assert brain_region.label == 'brain_stem'
    # brain_network.add_edge('brain_stem', 'thalamus', 3)
    # brain_network.add_edge('brain_stem', 'amigdala', 5)
    # brain_network.add_edge('brain_stem', 'hypocampus', 5 )
    # brain_network.add_edge('thalamus', 'frontal_lobe', 5)
    # brain_network.add_edge('amigdala', 'frontal_lobe', 8)
    # brain_network.add_edge('hypocampus', 'frontal_lobe', 10)
    # assert brain_network.traverse() == ['brain_stem','hypocampus','amigdala','frontal_lobe']
    # assert brain_network.edges_weights_sum('amigdala') == 8
    # assert brain_network.edges_weights_sum('frontal_lobe') == 0
    # assert brain_network.edges_weights_sum('hypocampus') == 10
    # assert brain_network.edges_weights_sum('thalamus') == 5
    # assert brain_network. edges_weights_sum('brain_stem') == 13
    # assert brain_network.get_neighbors('brain_stem') == ['hypocampus', 'amigdala', 'thalamus']
    # assert brain_network.most_connected_path('brain_stem','frontal_lobe') == ['brain_stem' , 'hypocampus', 'frontal_lobe', 15]
    # assert brain_network.least_connected_path('brain_stem','frontal_lobe') == ['brain_stem', 'thalamus', 'frontal_lobe', 8]


test_Graph()

# TODO adding edges functionality to the graph
