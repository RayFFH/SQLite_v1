import databasescoding

i = 1

while(i == 1):
    ans = input("""
    Please pick from the following options 
    1 to show
    2 to add
    3 to delete
    4 to search
    5 to delete whole table
            """)

    if int(ans) == 1:
        databasescoding.show_record()
    elif int(ans) == 2:
        first = input("first name?")
        last = input("last name?")
        age = input("age?")
        databasescoding.add(first, last, age)
    elif int(ans) == 3:
        ans = input("What ID do you want to delete?")
        databasescoding.delete(ans)
    elif int(ans) == 4:
        first = input("first name?")
        databasescoding.name_finder(first)
    elif int(ans) == 5:
        databasescoding.drop()
    else:
        i = 2

print("Ending program")