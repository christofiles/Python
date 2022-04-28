print("MENU")
print("1. Count letters in the string")
print("2. Count uppercase, lowercase, vowels & digits in the string")
print("3. Reverse the string and check whether it is a palindrome")


string=input('Enter string: ')

while True:
    choice = int(input("Enter your choice:"))

    if choice == 1:
        ct = 0

        for i in string:
            asc = ord(i)
            if asc >= 65 and asc <=90 or asc >=97 and asc <=122:
                ct+=1

        print("The count is", ct)

    elif choice == 2:
        ul = 0
        ll = 0
        vowels = 0
        digits = 0
        vowelsl = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]

        for i in string:
            asc = ord(i)

            if asc >= 65 and asc <= 90:
                ul += 1
            if asc >= 97 and asc <= 122:
                ll += 1
            if asc >= 48 and asc <= 57:
                digits += 1
            if i in vowelsl:
                vowels += 1
        print("Uppercase letters:", ul)
        print("Lowercase letters:", ll)
        print("Digits:", digits)
        print("Vowels:", vowels)

    elif choice == 3:
        reverse = string[::-1]
        print("The reverse is", reverse)
        if reverse == string:
            print("The string is a palindrome")
        else:
            print("The string is not a palindrome")

    elif choice == 4:
        print("Exiting...")
        break

    else:
        print("Invalid choice")