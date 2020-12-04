import graph_algorithms
import random, string
from graph_algorithms import Algorithms


def create_random_string():
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(5))


def test_create_random_string():
    random_string = create_random_string()
    assert len(random_string) == 5
    assert type(random_string) == str


test_create_random_string()

