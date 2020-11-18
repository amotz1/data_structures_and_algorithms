import mergesort
import graph_algorithms
from graph_algorithms import Algorithms


def create_test_graph():
    brain_network = graph_algorithms.Graph()
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
    isolated_cities = graph_algorithms.Graph()
    for city in ['jerusalem', 'haifa']:
        isolated_cities.create_vertex(city)
    return isolated_cities


def create_test_graph_2():
    two_pairs_of_cities = graph_algorithms.Graph()
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
    israel_cities = graph_algorithms.Graph()
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
    israel_cities = graph_algorithms.Graph()
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


def create_brute_force_graph():
    israel_cities = graph_algorithms.Graph()
    haifa = israel_cities.create_vertex('haifa')
    naharia = israel_cities.create_vertex('naharia')
    rishon = israel_cities.create_vertex('rishon')
    eilat = israel_cities.create_vertex('eilat')
    israel_cities.create_edge(haifa, naharia, 10)
    israel_cities.create_edge(haifa, rishon, 2)
    israel_cities.create_edge(rishon, eilat, 12)
    israel_cities.create_edge(rishon, naharia, 1)
    israel_cities.create_edge(naharia, eilat, 30)
    return israel_cities


def test_correct_path(edges, correct_edges_attributes):
    assert len(edges) == len(correct_edges_attributes)
    for edge, attributes in zip(edges, correct_edges_attributes):
        # comparing each edge vertex attribute to either one of two vertices because edges are bi-directional
        assert edge.vertex_1 == attributes[0] and edge.vertex_2 == attributes[1] \
               or edge.vertex_2 == attributes[0] and edge.vertex_1 == attributes[1]
        assert edge.length == attributes[2]


def is_path(edges, source, dest):
    vertex = source
    for edge in edges:
        vertex = edge.get_other_vertex(vertex)
    return vertex == dest


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

    israel_cities = create_brute_force_graph()
    haifa = israel_cities.get_vertex('haifa')
    rishon = israel_cities.get_vertex('rishon')
    naharia = israel_cities.get_vertex('naharia')
    eilat = israel_cities.get_vertex('eilat')

    haifa_naharia = haifa.edges[0]
    assert haifa_naharia.get_other_vertex(haifa) == naharia
    assert haifa_naharia.get_other_vertex(naharia) == haifa

    haifa_rishon = haifa.edges[1]
    assert haifa_rishon.get_other_vertex(haifa) == rishon
    assert haifa_rishon.get_other_vertex(rishon) == haifa

    rishon_naharia = rishon.edges[2]
    assert rishon_naharia.get_other_vertex(naharia) == rishon
    assert rishon_naharia.get_other_vertex(rishon) == naharia

    rishon_eilat = rishon.edges[1]
    assert rishon_eilat.get_other_vertex(eilat) == rishon
    assert rishon_eilat.get_other_vertex(rishon) == eilat

    naharia_eilat = naharia.edges[2]
    assert naharia_eilat.get_other_vertex(naharia) == eilat
    assert naharia_eilat.get_other_vertex(eilat) == naharia

    assert Algorithms.compute_all_paths(haifa, eilat) == [[haifa_naharia, rishon_naharia, rishon_eilat],
                                                          [haifa_naharia, naharia_eilat],
                                                          [haifa_rishon, rishon_eilat],
                                                          [haifa_rishon, rishon_naharia, naharia_eilat]]

    (min_path_length, min_path) = Algorithms.shortest_path_bf(haifa, eilat)
    assert min_path_length == 14

    (shortest_path_length, shortest_path) = Algorithms.shortest_path_bf(haifa, haifa)
    assert shortest_path_length == 0
    assert shortest_path == []

    paths = []
    Algorithms._compute_all_paths(naharia, eilat, [haifa_naharia], paths)
    print(paths)

    israel_cities = create_test_cities()
    haifa = israel_cities.get_vertex('haifa')
    rishon = israel_cities.get_vertex('rishon')
    beer_sheva = israel_cities.get_vertex('beer_sheva')
    naharia = israel_cities.get_vertex('naharia')
    eilat = israel_cities.get_vertex('eilat')

    (shortest_path_length, shortest_path) = Algorithms.shortest_path(haifa, haifa)
    (shortest_path_length_bf, shortest_path_bf) = Algorithms.shortest_path_bf(haifa, haifa)

    assert shortest_path_length == shortest_path_length_bf
    assert shortest_path == shortest_path_bf
    assert shortest_path_length == 0
    assert is_path(shortest_path, haifa, haifa)

    correct_edges_attributes = []
    test_correct_path(shortest_path, correct_edges_attributes)

    (shortest_path_length, shortest_path) = Algorithms.shortest_path(haifa, rishon)
    (shortest_path_length_bf, shortest_path_bf) = Algorithms.shortest_path_bf(haifa, rishon)

    assert shortest_path_length == shortest_path_length_bf
    assert shortest_path == shortest_path_bf
    assert shortest_path_length == 40
    assert is_path(shortest_path, haifa, rishon)

    correct_edges_attributes = [(haifa, rishon, 40)]
    test_correct_path(shortest_path, correct_edges_attributes)

    (shortest_path_length, shortest_path) = Algorithms.shortest_path(rishon, haifa)
    (shortest_path_length_bf, shortest_path_bf) = Algorithms.shortest_path_bf(rishon, haifa)

    assert shortest_path_length == shortest_path_length_bf
    assert shortest_path == shortest_path_bf
    assert shortest_path_length == 40
    assert is_path(shortest_path, rishon, haifa)

    correct_edges_attributes = [(rishon, haifa, 40)]
    test_correct_path(shortest_path, correct_edges_attributes)

    (shortest_path_length, shortest_path) = Algorithms.shortest_path(haifa, eilat)
    (shortest_path_length_bf, shortest_path_bf) = Algorithms.shortest_path_bf(haifa, eilat)

    assert shortest_path_length == shortest_path_length_bf
    assert shortest_path == shortest_path_bf
    assert shortest_path_length == 90
    assert is_path(shortest_path, haifa, eilat)

    correct_edges_attributes = [(haifa, rishon, 40), (rishon, beer_sheva, 20), (beer_sheva, naharia, 20),
                                (naharia, eilat, 10)]

    test_correct_path(shortest_path, correct_edges_attributes)

    israel_cities = create_test_cities_1()
    haifa = israel_cities.get_vertex('haifa')
    eilat = israel_cities.get_vertex('eilat')
    petach_tikva = israel_cities.get_vertex('petach_tikva')
    (shortest_path_length, shortest_path) = Algorithms.shortest_path(haifa, eilat)
    (shortest_path_length_bf, shortest_path_bf) = Algorithms.shortest_path_bf(haifa, eilat)

    assert shortest_path_length == shortest_path_length_bf
    assert shortest_path == shortest_path_bf
    assert shortest_path_length == 3

    correct_edges_attributes = [(haifa, petach_tikva, 2), (petach_tikva, eilat, 1)]
    test_correct_path(shortest_path, correct_edges_attributes)
    assert is_path(shortest_path, haifa, eilat)

    # TODO optimizing path_vartices to be a hashtable  for better performance in find_path_vertices function.
    # TODO maybe trying to avoid the find_path_vertices and using lambda instead for lazy evaluation
    # TODO making the reccursion call return a list of paths instead of an output parameter



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