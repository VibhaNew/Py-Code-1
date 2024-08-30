age = input("age: ")

if(age>="18" and age < "60"):
    print("Vote")
elif(age<"18"):
    print("Underage")
else:
    print("Senior Citizen")