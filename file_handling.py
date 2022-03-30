#f = open("employees.txt")
#print(type(f))
#print(f.read())
#f.close()  # pay attention to close the file

with open("employees.txt", encoding="utf-8") as f:  # a with gondoskodik róla, hogy a file le is legyen tárva
    #print(type(f))
    #print(f.read())
    for line in f:  # soronkénti beolvasás
        #print(line, end="")
        print(line.strip())

# mindig figyeljünk a karakterkódolásra
with open("employees_temp.txt", "w", encoding="utf-8") as f:  # w -write into new file, a- append exisiting file
    f.write("John Doe\n")
    f.write("JAck Doe\n")

