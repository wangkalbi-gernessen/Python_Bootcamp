import random
from country_list import country_list

stages = []

chosen_country = random.choice(country_list).lower()
print(chosen_country)

display = []
for _ in range(len(chosen_country)):
    display.append("_")

lives = 10
end_of_game = False

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    for position in range(len(chosen_country)):
        char = chosen_country[position]
        if char == guess:
            display[position] = char 

    print(display)
    
    if guess not in chosen_country:
        print(f"You guessed {guess}, but it's not in the word. You lose a life.")
        lives -= 1
        if lives == 0: 
            end_of_game = True
            print("You lose!")
    
    if "_" not in display:
        end_of_game = True
        print("You win!!")