# NUMBER GUESSING GAME

secret_number = int(input("secret_number : "))

number_of_chances = 0
maximum_number_of_chances = 3

while (number_of_chances < maximum_number_of_chances ) :
    guess = int(input("Guess : "))
    number_of_chances += 1
    if (secret_number == guess):
        print(f"CONTRATULATIONS! , YOU WON THE GAME AT GUESS_NUMBER {number_of_chances} READY TO COLLECT THE REWARDS ?")
        break
else :
    print("YOU ARE OUT OF CHANCES!! , READY FOR A BONUS GUESS ;")
 

def bonus_guess():
    if (guess != secret_number):
        final_guess = int(input("Final_guess : "))
        if (final_guess > secret_number):
            print(f"TOO BIG ,{secret_number} is the secret number")
        elif (final_guess < secret_number):
            print(f"TOO SMALL ,{secret_number} is the secret number ")
        else :
            print("CONTRATULATIONS! , YOU WON , READY TO COLLECT THE REWARDS ?")
    return
bonus_guess()

print("!!END OF THE GAME!!")

