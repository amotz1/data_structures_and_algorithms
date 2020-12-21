import algorithms.graph_algorithms as graph_algorithms
from algorithms.graph_algorithms import Graph
from algorithms.graph_algorithms import Algorithms
import sys


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



def test_shortest_path_algorithms():
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

    # basic functionality test graph

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

    # the graph i create below is a test case to a bug related to the condition for stopping the while loop
    # in shortest_path function of the grath algorithms file.
    # (stopping the while loop if dest is smaller then the max or min path lengths of paths that i developed)

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

    (shortest_path_length, shortest_path) = Algorithms.shortest_path(haifa, eilat)
    (shortest_path_length_bf, shortest_path_bf) = Algorithms.shortest_path_bf(haifa, eilat)

    assert shortest_path_length == shortest_path_length_bf
    assert shortest_path == shortest_path_bf
    assert shortest_path_length == 3

    correct_edges_attributes = [(haifa, petach_tikva, 2), (petach_tikva, eilat, 1)]
    test_correct_path(shortest_path, correct_edges_attributes)
    assert is_path(shortest_path, haifa, eilat)

    # checking a test case of a graph with unreachable dest
    unreachable_test_graph = Graph()
    x = unreachable_test_graph.create_vertex('dummy')
    y = unreachable_test_graph.create_vertex('dummy')
    assert Algorithms.shortest_path(x, y) == (sys.maxsize, None)
    assert Algorithms.shortest_path_bf(x, y) == (sys.maxsize, None)

    # checking a test case of a graph with 2 edges between 2 vertices
    israel_cities = Graph()
    haifa = israel_cities.create_vertex('haifa')
    rishon = israel_cities.create_vertex('rishon')
    eilat = israel_cities.create_vertex('eilat')
    haifa_rishon1 = israel_cities.create_edge(haifa, rishon, 10)
    haifa_rishon2 = israel_cities.create_edge(haifa, rishon, 6)
    rishon_eilat = israel_cities.create_edge(rishon, eilat, 10)

    assert haifa.get_edges() == [haifa_rishon1, haifa_rishon2]
    assert rishon.get_edges() == [haifa_rishon1, haifa_rishon2, rishon_eilat]
    assert eilat.get_edges() == [rishon_eilat]

    assert Algorithms.shortest_path(haifa, eilat) == (16, [haifa_rishon2, rishon_eilat])
    assert Algorithms.shortest_path_bf(haifa, eilat) == (16, [haifa_rishon2, rishon_eilat])


test_shortest_path_algorithms()

# TODO optimizing path_vartices to be a hashtable  for better performance in find_path_vertices function.
# TODO maybe trying to avoid the find_path_vertices and using lambda instead for lazy evaluation
# TODO making the recursion call return a list of paths instead of an output parameter
# TODO making random_graph and comparing shortest_path_bf with shortest_path

