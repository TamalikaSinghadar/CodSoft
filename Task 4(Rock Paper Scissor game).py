import random

l=['rock','paper','scissor']
cm=0;
um=0;
print("GAME STARTS")
count=int(input("How many rounds you wanna play?"))
for a in range(1,count+1):
    print("\n***************************")
    print("Round "+str(a))
    print("---------------------------")
    user=int(input("Enter your choice:\n1-Rock\n2-paper\n3-Scissor\n"))
    if user==1:
        print("User chose rock")
    elif user==2:
        print("User chose paper")
    elif user==3:
        print("User chose scissor")
    else:
        print("Invalid input")
        exit()

    c=random.choice(l)
    print("Computer chose "+c)

    if user==1 and c==l[0]:
        print("DRAW!!!")
        print("\n")
        print(" ----------------")
        print("|user= "+str(um)+"         |")
        print("|Computer= "+str(cm)+"     |")
        print(" ----------------")
        
    
    elif user==1 and c==l[1]:
        print("computer wins\npaper covers rock!!!")
        cm+=1;
        print("\n")
        print(" ----------------")
        print("|user= "+str(um)+"         |")
        print("|Computer= "+str(cm)+"     |")
        print(" ----------------")
        
    elif user==1 and c==l[2]:
        print("user wins\nRock destroys scissor!!!")
        um+=1;
        print("\n")
        print(" ----------------")
        print("|user= "+str(um)+"         |")
        print("|Computer= "+str(cm)+"     |")
        print(" ----------------")
        
         
    elif user==2 and c==l[0]:
         print("User wins\npaper covers rock!!!")
         um+=1;
         print("\n")
         print(" ----------------")
         print("|user= "+str(um)+"         |")
         print("|Computer= "+str(cm)+"     |")
         print(" ----------------")
        
    elif user==2 and c==l[1]:
         print("DRAW!!!")
         print("\n")
         print(" ----------------")
         print("|user= "+str(um)+"         |")
         print("|Computer= "+str(cm)+"     |")
         print(" ----------------")
        
    elif user==2 and c==l[2]:
         print("Computer wins wins\nscissor cuts paper!!!")
         cm+=1;
         print("\n")
         print(" ----------------")
         print("|user= "+str(um)+"         |")
         print("|Computer= "+str(cm)+"     |")
         print(" ----------------")
        
    elif user==3 and c==l[0]:
         print("Computer wins\nRock destroys scissor!!!")
         cm+=1;
         print("\n")
         print(" ----------------")
         print("|user= "+str(um)+"         |")
         print("|Computer= "+str(cm)+"     |")
         print(" ----------------")
        
    elif user==3 and c==l[1]:
         print("User wins wins\nscissor cuts paper!!!")
         um+=1;
         print("\n")
         print(" ----------------")
         print("|user= "+str(um)+"         |")
         print("|Computer= "+str(cm)+"     |")
         print(" ----------------")
        
    else:
         print("DRAW!!!")
         print("\n")
         print(" ----------------")
         print("|user= "+str(um)+"         |")
         print("|Computer= "+str(cm)+"     |")
         print(" ----------------")
        
print("\nFINAL SCORE:\nUser:"+str(um)+"\nComputer:"+str(cm))
if um>cm:
    print("\nWINNER: User")
elif cm>um:
    print("\nWINNER: Computer")
else:
    print("\nDRAW")
print("Thank You for playing")
    
