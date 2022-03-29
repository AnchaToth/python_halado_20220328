import pytest
from own_exception_demo import calculate_age

from own_exception_demo import calculate_age

def test_calculate_age():
    assert calculate_age(1990, 2022) == 32

def test_calculate_age_where_year_of_birth_larger_than_actual_year():
    #try:
    #    calculate_age(1990, 1920)
    #    assert False  # mivel ennek kivételt kell dobnie, ha nem dob, akkor a False buktatja a tesztet
    #except ValueError as e:
    #    assert str(e) == "A szuletesi ev nem lehet kisebb, mint az aktualis ev"

    with pytest.raises(ValueError) as e:  # ilyenkor az e = exception info, nem az aktuális üzenet
        calculate_age(1980, 1902)
    assert str(e.value) == "A szuletesi ev nem lehet kisebb, mint az aktualis ev"
