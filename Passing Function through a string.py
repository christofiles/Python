def str_update(s):
    s1 = ""
    for i in s:
        if i.isupper():
            s1 = s1 + i.lower()                          
        if i.islower():
            s1+= i.upper()
        if i.isdigit():
            s1+='@'
        if i.isspace():
            s1 += "*"
    return s1


s = input("Enter : ")
print(str_update(s))
str_update(s)