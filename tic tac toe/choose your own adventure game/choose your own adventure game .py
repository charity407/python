name = input("Type your name: ")
print("Welcome" ,name ,"to this adventure")


Answer = print("You are on the dirt road, it has come to te end and you can go left or right.Which way would you like to go? ").lower()

if Answer == "left":
    Answer = input("You came to a river , you can walk around or swim across? Type walk to walk around and swim to swim across: ")
    if Answer == "swim":
        print("You were eaten by a crocodile! You lose! ")
    elif Answer == "walk":
        print("You walked for too long,you ran out of water,you lose!")
    else:
        print("Invalid option.You lose!")

elif Answer == "right":
    Answer = input("You come to a bridge, it loks wobbly,do you want to cross it or head back (cross/back)?")
    if Answer == "back":
        print("You go back and lose!")
    elif Answer == "cross":
        print("You cross the road and meet a stranger , do you talk to them? ")
        if Answer == "yes":
            print("You talk to the stranger and they give you gold.YOU WIN! ")
        elif Answer == "no":
            print("You lose! ")
        else:
            print("Invalid option.You lose!")
    else:
        print("Invalid option.You lose!")

        print("Thank you for trying" ,name, ".")
