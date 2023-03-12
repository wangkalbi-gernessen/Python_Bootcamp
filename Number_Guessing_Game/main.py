from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(guess, answer, turns):
    if guess > answer:
        print("Too high.")    
        turns -= 1
        return turns
    elif guess < answer:
        print("Too low.")
        turns -= 1
        return turns
    else:
        print(f"You got it!! The answer is {answer}.")

def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else: 
        return HARD_LEVEL_TURNS

def game():
    print("Welcome to Number Guessing Game! ")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)
    # print(f"Pssst, the correct answer is {answer}.")
    turns = set_difficulty()

    guess = 0
    while guess != answer: 
        print(f"You have {turns} attempts remaining to guess the number.")
        
        guess = int(input("Make a guess: "))

        turns = check_answer(guess, answer, turns)
        if turns == 0: 
            print("You've run out of guesses, you lose.")
        elif guess != answer:
            print("Guess again!")
        
game()