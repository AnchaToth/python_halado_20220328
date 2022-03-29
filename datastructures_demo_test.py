from datastructures_demo import find_all_occurences


def test_find_all_occurances_normal():
    assert find_all_occurences("almaalmaalmalma", "alma") == [0, 4, 8]


def test_find_all_occurances_overlap():
    assert find_all_occurences("XXXX", "XX") == [0, 2]


def test_find_all_occurances_not_found():
    assert find_all_occurences("almaalmaalmalma", "X") == []
