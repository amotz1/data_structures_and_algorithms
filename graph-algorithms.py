import linked_list

class Graph:
    def __init__(self):
        self.list = []

    def add_vertex(self, label):

    def add_edge(self, src, dest):

    def traverse(self):

    def efferent_neurons_sum(self):

    def get_neighbors(self):

    def most_connected_path(self):

    def least_connected_path(self):





class Vertex:
    def __init__(self):



class Edge:
    def __init__(self):


def test_Graph():
    brain_network = Graph()
    brain_network.add_vertex('hypocampus')
    assert brain_network.find_vertex('hypocampus') == hypocampus
    brain_network.add_vertex('thalamus')
    assert brain_network.find_vertex('thalamus') == thalamus
    brain_network.add_vertex('amigdala')
    assert brain_network.find_vertex('amigdala') == amigdala
    brain_network.add_vertex('frontal_lobe')
    assert brain_network.find_vertex('frontal_lobe') == frontal_lobe
    brain_network.add_vertex('brain_stem')
    brain_network.add_edge('brain_stem', 'thalamus', 3)
    brain_network.add_edge('brain_stem', 'amigdala', 5)
    brain_network.add_edge('brain_stem', 'hypocampus', 5 )
    brain_network.add_edge('thalamus', 'frontal_lobe', 5)
    brain_network.add_edge('amigdala', 'frontal_lobe', 8)
    brain_network.add_edge('hypocampus', 'frontal_lobe', 10)
    assert brain_network.traverse() == ['brain_stem','hypocampus','amigdala','frontal_lobe']
    # efferent nerves are neurons that goes from the vertex out to other vertcies (like edges weight)
    assert brain_network.efferent_neurons_sum('amigdala') == 8
    assert brain_network.efferent_neurons_sum('frontal_lobe') == 0
    assert brain_network.efferent_neurons_sum('hypocampus') == 10
    assert brain_network.efferent_neurons_sum('thalamus') == 5
    assert brain_network.efferent_neurons_sum('brain_stem') == 13
    assert brain_network.get_neighbors('brain_stem') == ['hypocampus', 'amigdala', 'thalamus']
    assert brain_network.most_connected_path('brain_stem','frontal_lobe') == ['brain_stem' , 'hypocampus', 'frontal_lobe', 15]
    assert brain_network.least_connected_path('brain_stem','frontal_lobe') == ['brain_stem', 'thalamus', 'frontal_lobe', 8]

