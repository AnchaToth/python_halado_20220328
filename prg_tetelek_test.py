from prg_tetelek import count_accented, count_accented_new, find_names_with_J, get_absolute_values, longest_word, sum_numbers, check_for_natural_numbers

def test_sum():
    #given
    numbers = [1,2,3,4,5]
    #when
    result = sum_numbers(numbers)
    #then 
    #összehasonlítjuk az elvárt értéket a kapott értékkel
    assert result == 15

# Assert sum_numbers([1,2,3,4,5]) == 12

def test_count_accented():
    assert count_accented("akármicsakékezetes") == 2

def test_count_accented_2():
    assert count_accented_new("akármicsakÉkezetesbetű") == 3
    assert count_accented_new("elégMÁRazÉkezetekből") == 4

def test_longest_word():
    assert longest_word("valamit írok ide csak hogy teszteljek") == "teszteljek"

def test_check_for_natural_numbers():
    assert check_for_natural_numbers([3,7,5,2,1])

def test_check_for_natural_numbers_negativ():
    assert not check_for_natural_numbers([3,7,5,-2,1])

def test_check_for_natural_numbers_null():
    assert not check_for_natural_numbers([3,7,5,0,1])

def test_find_names_with_J():
    assert find_names_with_J(["Joe","Karla","Tom","James"]) == ["Joe","James"]

def test_find_names_with_J_non_capital():
    assert find_names_with_J(["Joe","Karla","Tom","james"]) == ["Joe","james"]

def test_get_absolute_values():
    assert get_absolute_values([3,-2,-5,8,-18]) == [3,2,5,8,18]