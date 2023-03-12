from game_data import data 
import random 

# Format the account data into printable format 
def format_data(account):
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    print(f"{account_name}, a {account_descr}, from {account_country}")

def check_answer(guess, a_followers, b_followers):
    """Use if statement to check if user is correct"""
    if a_followers > b_followers: 
        if guess == 'a':
            return guess == 'a'
        else: 
            return guess == 'b'
            

# Display art
score = 0
game_should_continue = True 

# Make the game repeatable
while game_should_continue:

    # Generate a random account from the game data

    # Making account at position B become the next account at position A
    account_a = random.choice(data)
    account_b = random.choice(data)

    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}.")
    print(f"Compare B: {format_data(account_b)}.")

    # Ask user for a guess
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # Check if user is correct 
    ## Get follower count of each account
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    # Clear screen between rounds

    # Give user feedback on their guess
    # Score keeping
    if is_correct:
        score += 1
        print("You are right! Current score: {score}.")
    else:
        game_should_continue = False 
        print("Sorry, that's wrong. Final score: {score}.")








