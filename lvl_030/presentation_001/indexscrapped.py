import turtle
turtle_bank=turtle.Turtle()
turtle_flower1=turtle.Turtle()
turtle_flower2=turtle.Turtle()
turtle_bank.hideturtle()
turtle_flower1.hideturtle()
turtle_flower2.hideturtle()

print("=== REGISTRATION ===")
login_user=input("Insert name: ")
login_password=input("Insert password [Password must be below 20 characters]: ")
while len(login_password)>20 or len(login_password)<1:
    print("INVALID, TRY AGAIN")
    login_password=input("Insert password [Password must be below 20 characters]: ")
print("Welcome",login_user.capitalize())

print()
print("LOADING...")
print()

turtle_bank.penup()
turtle_flower1.penup()
turtle_flower2.penup()
turtle_bank.color("darkgreen")
turtle_flower1.color("pink")
turtle_flower2.color("pink")
turtle_bank.goto(-100,100)
turtle_flower1.goto(-300,50)
turtle_flower2.goto(300,50)

turtle_bank.showturtle()
turtle_bank.pendown()
turtle_bank.goto(100,100)
turtle_bank.goto(100,-100)
turtle_bank.goto(-100,-100)
turtle_bank.goto(-100,100)
turtle_bank.penup()
turtle_bank.goto(-30,0)
turtle_bank.pendown()
turtle_bank.write("GOA BANK")
turtle_bank.hideturtle()

turtle_flower1.showturtle()
turtle_flower1.pendown()
turtle_flower1.goto(-250,50)
turtle_flower1.goto(-250,25)
turtle_flower1.goto(-300,25)
turtle_flower1.goto(-300,50)
turtle_flower1.penup()
turtle_flower1.goto(-270,25)
turtle_flower1.pendown()
turtle_flower1.color("green")
turtle_flower1.goto(-270,-50)
turtle_flower1.hideturtle()

turtle_flower2.showturtle()
turtle_flower2.pendown()
turtle_flower2.goto(250,50)
turtle_flower2.goto(250,25)
turtle_flower2.goto(300,25)
turtle_flower2.goto(300,50)
turtle_flower2.penup()
turtle_flower2.goto(270,25)
turtle_flower2.pendown()
turtle_flower2.color("green")
turtle_flower2.goto(270,-50)
turtle_flower2.hideturtle()

print("LOADING COMPLETE")

real_money=float(200)
bank_money=float(100)
debt=float(0)

while True:
    print()
    print("=== GOA BANK ===")
    print("1) Check Money:")
    print("2) Deposit Money:")
    print("3) Withdraw Money:")
    print("4) Get Loan")
    print("5) Pay Debt")
    print("6) Leave System:")

    choice=int(input("Enter your choice: "))

    if choice==1:
        print()
        print("Checking money...")
        print("You have",bank_money,"dollars in your bank and",real_money,"dollars in your wallet")

    elif choice==2:
        print()
        print("Depositing money...")
        if real_money<0:
            print("You don't have any money in your walet!")
        else:
            while deposited<real_money:
                deposited=float(input("How much money do you want to deposit? "))
                if deposited>real_money:
                    print("INVALID DEPOSIT, TRY AGAIN")
            bank_money=bank_money+deposited
            real_money=real_money-deposited
            print("You now have",bank_money,"dollars in your bank and",real_money,"dollars in your wallet")
        print()

    elif choice==3:
        print()
        print("Withdrawing money...")
        if bank_money<0:
            print("You don't have any money in your bank!")
        else:
            withdrew=float(input("How much money do you want to withdraw? "))
            if withdrew>bank_money:
                print("You're in debt!")
                debt=debt+bank_money
            bank_money=bank_money-withdrew
            real_money=real_money+withdrew
            print("You now have",bank_money,"dollars in your bank and",real_money,"dollars in your wallet")
        print()

    elif choice==4:
        print("Loaning money...")
        loaned=float(input("How much money do you want to loan? "))
        debt=loaned+debt
        print("You now have",bank_money,"dollars in your bank and",debt,"dollars to pay back")

    elif choice==5:
        print()
        print("Paying debt...")
        if debt<1:
            print("There's no debt for you to pay!")
        else:
            debted=float(input("How much money do you want to pay back to your debt? "))
            if debted<1 or debted!=float:
                print("INVALID, MAYBE PAY NEXT TIME")
            else:
                debted=debted+bank_money
                if debted<0:
                    print("You'll be getting a interest!")
                    bank_money=bank_money-debted+10
                    debted=0
                elif debted>0:
                    print("You still got a lot to pay back for your debt...")
                else:
                    print("Congrats! You payed your debt completely!")
                print("You now have",bank_money,"dollars in your bank account")
        print()
    
    elif choice==6:
        print()
        print("Exiting bank...")
        print("Goodbye!")
        print()
        break

    else:
        print("INVALID VALUE, TRY AGAIN")