# This is a program to make a Scissor paper Rock.
# You will paly against the computer
# S = Scissor , R = Rock , P = Paper

# if player and computer chose same ...then the game is said to be tie! , you will have to play again 



# import random module

import random



print("Winning Rules of the Rock paper scissor game as follows: \n\n"
+"\nRock vs paper  ->  paper wins \n"
+"Rock vs scissor  ->  Rock wins \n"
+"paper vs scissor ->  scissor wins \n")

while (True):

    print("Enter choice \n Rock (R) \n Scissor (S) \n Paper (P) \n")
    
    You = input("Your turn: ")
    You = You.upper()

    # If user input is invalid 
    # while :
    #     if (You != 'R' or You != 'S' or You != 'P'):
    #         print("Please Enter Valid Choice : ")
    #         You = input("Your turn: ")
    #         You = You.upper()

    if (You == 'R'):
        You = "Rock"
    elif (You == 'S'):
        You = "Scissor"
    elif (You == 'P'):
        You = "Paper"

    print("Your choice is: " + You)
    print("\nNow its computer turn.......")

    Comp_choice = ["Rock", "Paper", "Scissor"]
    Computer = random.choice(Comp_choice)
    print("Computer choice is: " + Computer)

    print(You + " V/s " + Computer)

    if (You == Computer) :
        print(" \n !!! Draw !!! \n")
        
    elif (You == "Paper") and (Computer == "Rock") :
        print("\n!!! You Win !!! \n")
    
    elif (You == "Rock") and (Computer == "Scissor") :
        print("\n !!! You Win !!! \n")
    
    elif (You == "Scissor") and (Computer == "Paper") :
        print("\n !!! You Win !!! \n")
    
    elif (You == "Scissor") and (Computer == "Rock") :
        print("\n !!! Computer Win !!! \n")
    
    elif (You == "Paper") and (Computer == "Scissor") :
        print("\n !!! Computer Win !!! \n")

    elif (You == "Rock") and (Computer == "Paper") :
        print("\n !!! Computer Win !!! \n")



