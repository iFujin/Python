import random
u=0
c=0
for i in range(int(input("how many times"))):

    user=int(input('1.rock\t2.paper\t3.scissor\t'))
    computer=random.randrange(1,4)
    if computer==1:
        print("computer enters: rock")
        if(user==1):
            print("tie")
        elif(user==2):
            print("User WIN")
            u=u+1
        elif(user==3):
            print("Computer WIN")
            c=c+1
    elif(computer==2):
        print("computer enters: paper")
        if(user==2):
            print("tie")
        elif(user==3):
            print("User WIN")
            u=u+1
        elif(user==1):
            print("Computer WIN")
            c=c+1
    elif(computer==3):
        print("computer enters: scissor")
        if(user==3):
            print("tie")
        elif(user==1):
            print("User Win")
            u=u+1
        elif(user==2):
            print("Computer WIN")
            c=c+1

print("User points :",u)
print("Computer points :",c)
if (u<c):
    print("Computer Wins")
elif (u>c):
    print("User Wins")
elif (u==c):
    print('Tie')