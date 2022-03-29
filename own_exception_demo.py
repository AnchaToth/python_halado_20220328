def calculate_age(year_of_birth, actual_year):
    if year_of_birth < 1900:
        raise ValueError(f"Hibas születési ev: {year_of_birth}, 1900-nal korabbi")
    if actual_year < 1900:
        raise ValueError(f"Hibas aktualis ev: {actual_year}, 1900-nal korabbi")
    if year_of_birth > actual_year:
        raise ValueError("A szuletesi ev nem lehet kisebb, mint az aktualis ev")
    return actual_year - year_of_birth

try:
    print(calculate_age(1990,2022))
    print(calculate_age(-5, 1990))
    #print(calculate_age(1992, 199))
    #print(calculate_age(1992, 1990))
except ValueError as e:
    print(e)