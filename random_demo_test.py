from random_demo import generate_lotto_numbers
from random import Random


def test_generate_lotto_numbers():
    assert generate_lotto_numbers(Random(12)) == [58, 5, 83, 88, 32]
