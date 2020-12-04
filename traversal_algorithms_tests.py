import mergesort
import graph_algorithms
from graph_algorithms import Algorithms


def create_test_Graph():
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


def test_isolated_cities():
    isolated_cities = graph_algorithms.Graph()
    for city in ['jerusalem', 'haifa']:
        isolated_cities.create_vertex(city)
    return isolated_cities


def test_two_pairs_of_cities():
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


def test_traversal_algorithms():
    brain_network = create_test_Graph()

    # vertex that is not in the_traversal
    assert brain_network.get_vertex('hillel') is None
    for vertex in ['hypocampus', 'thalamus', 'amygdala', 'frontal_lobe', 'brain_stem']:
        # every vertex  that we created is in the_traversal
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
    isolated_cities = test_isolated_cities()
    haifa = isolated_cities.get_vertex('haifa')
    jerusalem = isolated_cities.get_vertex('jerusalem')
    for city in [haifa, jerusalem]:
        dfs_vertices = Algorithms.dfs(city)
        rec_dfs_vertices = Algorithms.recursive_dfs(city)
        bfs_vertices = Algorithms.bfs(city)
        assert dfs_vertices == bfs_vertices
        assert rec_dfs_vertices == dfs_vertices

    two_pairs_of_cities = test_two_pairs_of_cities()
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


test_traversal_algorithms()

