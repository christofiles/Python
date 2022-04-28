T=eval(input('Enter tuple: '))
print('Tuple:\n', T)

while True:
    print('MENU')
    print('1. Add an element')
    print('2. Find the largest & smallest element')
    print('3. Update tuple')
    print('4. Search for an element')
    print('5. Exit')

    choice=int(input('Enter choice: '))

    if choice==1:
        n=int(input('Enter new element: '))
        T=T+(n,)
        print('Updated tuple:\n', T)

    elif choice==2:
        maxm=T[0]
        minm=T[0]
        for i in T:
            if i>maxm:
                maxm=i
            if i<minm:
                minm=i
        print('Largest element:', maxm)
        print('Smallest element:', minm)

    elif choice==3:
        L=list(T)
        for i in range(len(L)):
            if L[i]%2==0:
                L[i]=L[i]+2
            elif L[i]%2!=0:
                L[i]=L[i]+3
        nT=tuple(L)
        print('Updated Tuple:\n', nT)

    elif choice==4:
        n=int(input('Enter element to be searched: '))
        for i in range(len(T)):
            if n==T[i]:
                print('Item present in position:', i)
                break
            else:
                print('NOT FOUND')

    else:
        print("Exiting!")
        break