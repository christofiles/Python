n = int(input("Enter number of students: "))
d = {}
for i in range(n):
    adm = int(input("Enter admission number: "))
    role = input("Enter role number: ")
    name = input("Enter name: ")
    marks = input("Enter marks: ")
    d[adm] = [role, name, marks]



print(d)

adm = int(input("Search With Admission number: "))

print("Roll number : " ,d[adm][0])
print("Name :",d[adm][1])
print("Marks:", d[adm][2])
