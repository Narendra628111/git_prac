n=int(input())
for i in range(0,n):
    for j in range(0,n):
        if(j<i):
            print(" ",end=" ")
        else:
            if(j%2==0):
               print("@",end=" ")
            else:
               print("%",end=" ")
    print()


    



