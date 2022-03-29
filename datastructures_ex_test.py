from datastructures_ex import pick_every_other, replace_spec_chars

def test_pick_every_other():
    assert pick_every_other([2,5,4,8,9,3,0,6]) == [5, 8, 3, 6]

def test_pick_every():
    assert pick_every_other(["valami1", "valami2", "c3", "d4", "e5"]) == ["valami2", "d4"]

def test_pick_none():
    assert pick_every_other([]) == []

def test_replace_spec_chars():
    assert replace_spec_chars("akármicsakékezetszöveglegyen") == "akarmicsakekezetszoveglegyen"