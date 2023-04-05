A = input()
B = False
C = False
D = False
for i in A:
    F = i.isdigit()
    if F:
        D = True
A_U = (A.upper() == A)
if A_U == False:
    B = True
A_L = (A.lower() == A)
if A_L == False:
    C = True
        
if (B and C) and D:
    print("Valid Password")
else:
    print("Invalid Password")
    
