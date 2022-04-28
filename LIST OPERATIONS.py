print('MENU')
print('1. Count & sum of all odd numbers')
print('2. Count & sum of all even numbers')
print('3. Count the frequency of an element in the list')
print('4. Remove duplicate elements from the list')
print('5. Rotate the list')

choice=int(input('Enter choice of operation: '))

if choice==1:
    l=eval(input('Enter list (separate elements with a comma): '))
    print('1. Count & sum of all odd numbers\n')
    c=0
    s=0
    for i in l:
        if i%2!=0:
            c=c+1
            s=s+i
    
    print('Count of odd numbers:', c)
    print('Sum of odd numbers:', s)

elif choice==2:
    l=eval(input('Enter list (separate elements with a comma): '))
    print('2. Count & sum of all even numbers\n')
    c=0
    s=0
    for i in l:
        if i%2==0:
            c=c+1
            s=s+i
    
    print('Count of even numbers:', c)
    print('Sum of even numbers:', s)

elif choice==3:
    l=eval(input('Enter list (separate elements with a comma): '))
    print('3. Count the frequency of an element in the list\n')
    n=int(input('Enter element to be searched: '))
    c=0
    for i in l:
        if i==n:
            c=c+1

    print('Count of element,', n, 'in list:', c)

elif choice==4:
    print('4. Remove duplicate elements from the list\n')
    l1=eval(input('Enter list (separate elements with a comma): '))
    l2=[]
    for i in l1:
        if i not in l2:
            l2.append(i)

    print('New list (without duplicate elements):\n', l2)

elif choice==5:
    print('5. Rotate the list')
    l1=eval(input('Enter list (separate elements with a comma): '))
    print('Original list:', l1)
    l2=l1[-1:] + l1[:-1]
    print('Rotated list:', l2)
    