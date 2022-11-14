from random import randint


class Game():

    def __init__(self):
        self.choice()

    def choice(self):
        while True:
            print(
                "Welcome \n [1] Car Game \n [2] Rock Paper Scisor \n [3] Math Game")
            x = input("Enter Your Choice:")
            if x == "1":
                self.cargame()
            elif x == "2":
                self.r_p_s()
            elif x == "3":
                d = Arth()
            elif x == "quit":
                print("BYE BYE")
                break
            else:
                print("Wrong input Choose Again!!")
                continue

    def cargame(self):
        command = ""
        started = False
        while command != "quit":
            command = input("Car game started begin: ").lower()
            if command == "start":
                if started:
                    print("Car already started")
                else:
                    started = True
                    print('i`m ready to go')
            elif command == "stop":
                if not started:
                    print("Car is already stopped")
                else:
                    started = False
                    print('car stopped')
            elif command == "help":
                print("""
                    start => to start the car 
                    stop => to stop the car 
                    quit => to close the program and stop the car
                    """)
            elif command == "quit":
                print('car stopped')
                break
            else:
                print("i don`t understand that")

    def r_p_s(self):
        x1 = 1
        while True:
            x1 = input("Do you want to play ? y for yes , quit for no ")
            if x1 == "y":
                print("Enter The choice 1 for Rock - 2 for paper - 3 for scissor")
                choice = int(input("Enter your Choice: "))
                if choice < 1 or choice > 3:
                    print("invaliddddd number ")
                else:
                    if choice == 1:
                        choice_name = "Rock"
                    elif choice == 2:
                        choice_name = "Paper"
                    else:
                        choice_name = "Scissor"
                    print("user choice is :", choice_name)
                    comp_choice = randint(1, 3)
                    if comp_choice == 1:
                        comp_name = "Rock"
                    elif comp_choice == 2:
                        comp_name = "Paper"
                    else:
                        comp_name = "Scissor"
                    print("the computer choice is :", comp_name)
                    if choice == comp_choice:
                        print("Draw")
                    elif (choice == 1 and comp_choice == 2) or (choice == 3 and comp_choice == 1) or (choice == 2 and comp_choice == 3):
                        print("Computer Win")
                    else:
                        print("User Win")
            elif x1 == "quit":
                print("Bye Bye")
                break
            else:
                print("invalid number")


class Arth():

    def __init__(self):
        self.choice2()

    def choice2(self):
        try:
            while True:
                print(
                    "Welcome in math game \n [1] Odd or Even \n [2] Mul \n [3] Avg ")
                x = input("Enter Your Choice:")
                if x == "1":
                    self.o_e()
                elif x == "2":
                    self.mult()
                elif x == "3":
                    self.avg()
                elif x == "quit":
                    print("BYE BYE")
                    d = Game()
                else:
                    print("Wrong input Choose Again!!")
                    continue
        except:
            print('Try again')
            self.choice2()

    def o_e(self):
        new_number = int(input("Enter the value: "))
        if (new_number % 2) == 0:
            print("It is Even number".format(new_number))
        else:
            print("It is Odd number".format(new_number))

    def mult(self):
        n = int(input("Enter first Number  :"))
        m = int(input("Enter sec Number  :"))
        for x in range(n, m+1):
            for i in range(1, 13):
                value = x * i
                print(x, " * ", i, " = ", value)
            print("----------------------------------------")

    def avg(self):
        x = int(input("enter how many no."))
        list1 = []
        for i in range(1, x+1):
            f = int(input(f"enter {i}  : "))
            list1.append(f)
        sumOfNums = 0
        count = 0
        for number in list1:
            sumOfNums += number
            count += 1
        print(f"The Sum is {sumOfNums} and the avg is {sumOfNums/count}")


obj = Game()

