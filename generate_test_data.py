from random import choice, random, randint, Random

# írjatok egy olyan fv-t, amely 
# alkalmazottak listáját adja vissza!
# egy alkalmazott egy tuple legyen!
# legyen neve (tuple) és életkora
# név szerepeljen egy előnév és utónév listából választott értékből
#  életkor: 20-29 között

def pick_name():
    family_names = ["Kovács", "Szabó", "Fazekas", "Varga"]
    first_names = ["Álmos", "Előd", "Ond", "Kond", "Tas", "Huba", "Töhötöm"]

    name = (choice(first_names)+" "+choice(family_names))

    return name

def pick_age():  # random függvényt így nem tudjuk ellenőrizni
    return randint(20,29)

employees = []
number_of_employees = input("Add meg hány munkavállalót szeretnél generálni")
number_of_employees = int(number_of_employees)

for i in range(0,number_of_employees):
    employees.append(((pick_name()), pick_age()))

#print(employees)

# oktató
elonevek = ["Kovács", "Varga", "Fazekas", "Kádár", "Asztalos"]
utonevek = ["Ákos", "Ábel", "Ádám", "Bálint", "Bence"]


#def generate_employee(id, random=Random()):
#    return (id, choice(elonevek)+" "+choice(utonevek), randint(20,90))


#def generate_employees(number=5, random=Random()):
#    return [generate_employee(i, random) for i in range(number)]

#print(generate_employee(1))
#print(generate_employee())
# print(generat)
