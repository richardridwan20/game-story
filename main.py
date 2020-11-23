print("Welcome to my Game Story - where you can make your own story!")
print("Ah, I should introduce myself, my name is God.")

name = input("What is your name? ")
age = int(input("What is your age? "))

health = 10
attack = 2
salamander = 5

if age >= 18:
    print("You are allowed to enter the game.")
    print("You are starting with ", health, " health points and ", attack, " attack points.")

    wants_to_play = input("Do you want to play the game? (y/n) ").lower()
    
    if wants_to_play == "y":
        print("Please proceed.")
        print("You are stranded in a dessert with three weapons beside you. There are a sword, a shield and a gun.")
        
        ans = input("Which one do you pick? (sword/shield/gun) ")
        
        if ans == "sword":
            print("Great choice!")
            attack += 5
            print("Offensive, I see. Now you have ", health, " health points and ", attack, " attack points.")
            pass
        elif ans == "shield":
            print("Nice choice!")
            attack -= 1
            health += 10
            print("Oof, defensive. Now you have ", health, " health points and ", attack, " attack points.")
            pass
        elif ans == "gun":
            print("Risky choice!")
            attack += 10
            health -= 5
            print("Risk taker, I admire it. Now you have ", health, " health points and ", attack, " attack points.")
            pass
        pass
        
        print("You are greeted by a giant salamander with 5 health points. It hit you with 2 attack points!")
        health -= 2
        print("Oof, now you have ", health, " health points and ", attack, " attack points.")
        
        print("You attack the salamander with your weapon of choice!")
        salamander -= attack
        
        if salamander <= 0:
            print("Great! You defeated the salamander!")
            pass
        else:
            print("You lost the game..")
            pass
    
    else:
        print("Thank you, see you later!.")
        pass
    pass
else:
    print("I'm very sorry that you are not allowed to enter the game.")
    pass




'''
    string "hello", "hello world"
    bool True, False
    int 8, 7, -9, 10000
    float 9.1, 7.2, -9.8, -10.0
'''


