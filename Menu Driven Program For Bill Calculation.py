
bill = int(input("Enter The total Amount : "))

print("Choose an Option : ")
print("1. Payment by Credit card. -- 10% discount")
print("2. Payment by Debit card. -- 5% discount")
print("3. Payment by Net Banking -- 2% discount")
print("4. Other mode of payment. -- NO discount")

ch = int(input("Choose the mode of payment: "))

if ch==1:
    print("Credit card selected -- 10% Discount")
    d = bill * 0.10
    
elif ch==2:
    print("Debit card selected -- 5% Discount")
    d = bill * 0.05
    
elif ch==3:
    print("Net Banking selected -- 2% Discount")
    d = bill * 0.02
    
elif ch==4:
    print("Other mode of payment selected -- 10% Discount")
    d = bill * 0 

else :
    print("Invalid Option Selected!")
    
print("Discounted Amount :",d)
print("Total Bill Amount : ",bill - d)
