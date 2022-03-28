def mod_names(names):
    names[1] = "Jack XYZ"  # a fv tudja változtatni a paraméterül kapott listát


employees = ["John", "Jack", "Jane"]
mod_names(employees)

print(employees)

#----
def mod_name_str(name):
    name = "John Doe"  # 2) "JOhn Doe" literál létrejön a memóriába, az értékadás után a name már erre mutat

employee = "Jack Doe"
mod_name_str(employee)  # 1) létrejön a name változó a stack-en, hivatkozik a "Jack Doe"-ra
print(employee)


# ------
def remove_last(names):
    # names = names[0:-1]  # a szeletelés mindig egy új listát hoz létre, így az eredetit nem módosítja
    # names.remove(names[-1])
    # names = [name for name in names if name.startswith("Z")]
    # for name in names:
    #    if name.startswith("S"):
    #        names.remove(name)

employees = ["Zozo", "Zoe", "Zizi", "Steve"]
remove_last(employees)
print(employees)