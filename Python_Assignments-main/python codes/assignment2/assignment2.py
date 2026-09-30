def triangle(s1, s2, s3):
    if s1*2 + s22 == s3*2:
        print ("It is a right angled triangle.")
    elif s1*2 + s32 == s2*2:
        print("It is a right angled triangle.")
    elif s2*2 + s32 == s1*2:
        print("It is a right angled triangle.")
    else: 
        print("It is not a right angled triangle.")
s1=int(input("enter the length of the first side: "))
s2=int(input("Enter the length of the second side: "))
s3=int(input("Enter the length of the third side: "))
triangle(s1, s2, s3)