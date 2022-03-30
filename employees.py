class Employee:  # classoknál hazsnálunk nagybetűt

    def __init__(self, name, year_of_birth) -> None:  # lehet default értéket adni, akárcsak 1 függvénynél
        self.name = name  # az aktuális objektum memóriaterületére beírja a változó értékét
        self.year_of_birth = year_of_birth


    def get_age(self, actual_year):
        return actual_year - self.year_of_birth

    
    def __str__(self) -> str:  # megváltoztatjuk az objektum string reprezentációját
        return f"Employee({self.name}, {self.year_of_birth})"


#john = Employee()
#john.name = "John Doe"
#print(john)
#print(john.name)
#john.year_of_birth = 1990
#print(john.year_of_birth)

jack = Employee("Jack Smith", 1970)
print(jack)
print(jack.name)
print(jack.year_of_birth)
print(jack.get_age(2022))
