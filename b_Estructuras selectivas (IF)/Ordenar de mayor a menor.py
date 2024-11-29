A = 2 
B = 90 
C = 54

if (A > B):
    if (A > C):
        if (B > C):
            print(A,B,C)
        else:
            print(A,C,B)
    else:
        print(C,A,B)
else:
    if (B > C):
        if (A > C):
            print(B,A,C)
        else:
            print(B,C,A)
    else:
        print(C,B,A)