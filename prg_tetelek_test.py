from prg_tetelek import count_accent, count_accented_new, sum_numbers 

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
    assert count_accent("akármicsakékezetes") == 2

def test_count_accented_2():
    assert count_accented_new("akármicsakÉkezetesbetű") == 3