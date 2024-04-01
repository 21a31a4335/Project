def passwordchange(u):
    pin_c=int(input("enter pin:"))
    if(pin_c!=pin[username.index(u)]):
        print("invalid password")
        print("end")
    else:
        cp=input("enter ur current password:")
        if(cp!=password[username.index(u)]):
            print("password not match")
        else:
            np=input("enter new password:")
            cnp=input("confirm new password:")
            if(np==cnp):
                print("password changed successfully")
            else:
                print("password not matched")
                print("end")
def accountbalance(u):
    pin_c=int(input("enter pin:"))
    if(pin_c==pin[username.index(u)]):
        acb=acbalance[username.index(u)]
        print("account balance:",acb)
    else:
        print("invalid pin")
def deposit(u):
    am=am=int(input("enter amount:"))
    pin_c=int(input("enter ur pin:"))
    if(pin_c==pin[username.index(u)]):
        print("amount deposited")
        enqire=input("want  to know available balance? y/n: ")
        if(enqire=="y"):
            acb=acbalance[username.index(u)]-am
            print("available balanced:",acb)
        else:
            print("Thank you")
    else:
        print("invalid pin")
def withdraw(u):
    pin_c=int(input("enter ur pin:"))
    if(pin_c==pin[username.index(u)]):
        am=int(input("enter amount:"))
        if(am>acbalance[username.index(u)]):
            print("insuficient balance")
        else:
            print("collect amount")
            enqire=input("want  to know available balance? y/n: ")
            if(enqire=="y"):
                acb=acbalance[username.index(u)]-am
                print("available balanced:",acb)
            else:
                print("Thank you")
    else:
        print("invalid pin")
def correctpassword(x,y):
    if(x==password[username.index(y)]):
        flag=1
    if(flag==0):
        print("end")
    if(flag==1):
        print("1.withdraw")
        print("2.deposit")
        print("3.Balance")
        print("4.change password")
        while(1):
            choice=int(input("enter ur choice:"))
            if(choice in [1,2,3,4]):
                    break
            else:
                print("renter the choice")
        if(choice==1):
            withdraw(u)
        elif(choice==2):
            deposit(u)
        elif(choice==3):
            accountbalance(u)
        elif(choice==4):
            passwordchange(u)
username=['Aruna','Srinivasa','Sowmya']
password=['abc','def','ijk']
pin=[999,333,666]
acbalance=[10000,12000,1400]
u=input("enter username:")
if(u not in username):
    print("user not found")
    print("end")
else:
    p=input("enter password:")
    if(p not in password):
            print("no.of attemps 2")
            rep=input("reenter password:")
            if(rep not in password):
                print("no.of attemps 1")
                rep2=input("reenter password:")
                if(rep2 not in password):
                    print("account blocked")
                else:
                    correctpassword(rep2,u)
            else:
                correctpassword(rep,u)
    else:
        correctpassword(p,u)