user= int(input("Enter a Number Please:"))
arr=['Zero','One','Two','Three','Four','Five','Six','Seven','Eight','Nine']

if user>=0 and user<10:
   print("you enter 1 digit:",arr[user]) 

elif  user>9 and user<100:
    two=(int(user/10))+ (user%10)
    print("You enter two digit:",two)
    print("Sum is:",two)

elif user>100 and user<1000:
    a=int(user%10)
    b=int(user%100/10)
    c=int(user%1000/100)
    print("You enter three digit:",user)
    print("Multiply is:",a*b*c)

else :
    print("The number is out of range!")




