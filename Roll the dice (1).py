###ROLL THE DICE GAME###

import random
start_the_game = input(">>>")
continue_the_game = start_the_game.lower()
if (continue_the_game == "start"):
    while continue_the_game == "start":
        roll_the_dice = input("Roll the dice?? (y/n) :")
        for_all_cases = roll_the_dice.lower()
        if for_all_cases == "yes":
            first_number = random.randint(1 , 6)
            second_number = random.randint(1 , 6)
            print(f"({first_number} , {second_number})")
        elif for_all_cases == "no":
            print("!!!END OF THE GAME!!!")
            break
        else:
            print("Invalid value")
else:
    print("BYE✌️")

