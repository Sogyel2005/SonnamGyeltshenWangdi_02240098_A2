import random

# Global variables
overall_score = {
    "guess_number": 0,
    "rps": 0,
    "trivia": 0,
    "pokemon": 0
}
binder = {}

MAX_POKEDEX = 1025
CARDS_PER_PAGE = 64
ROWS = 8
COLUMNS = 8

# ---------------------- Function 1: Guess Number Game ----------------------
def guess_number_game():
    print("\n--- Guess the Number Game ---")
    number = random.randint(1, 100)
    guesses = 0
    correct = False

    while not correct:
        try:
            guess = int(input("Guess a number between 1 and 100: "))
            if guess < 1 or guess > 100:
                print("Please enter a number in the valid range.")
                continue
            guesses += 1
            if guess == number:
                print("Correct! You guessed it.")
                correct = True
            elif guess < number:
                print("Too low!")
            else:
                print("Too high!")
        except ValueError:
            print("Invalid input. Please enter an integer.")

    score = max(0, 10 - guesses)
    overall_score["guess_number"] += score
    print(f"Your score: {score}")

# ---------------------- Function 2: Rock Paper Scissors ----------------------
def rock_paper_scissors():
    print("\n--- Rock Paper Scissors ---")
    options = ['rock', 'paper', 'scissors']
    wins = 0

    for round_num in range(3):
        computer = random.choice(options)
        user = input("Choose rock, paper, or scissors: ").lower()
        if user not in options:
            print("Invalid choice.")
            continue
        print(f"Computer chose: {computer}")
        if user == computer:
            print("It's a tie!")
        elif (user == "rock" and computer == "scissors") or \
             (user == "scissors" and computer == "paper") or \
             (user == "paper" and computer == "rock"):
            print("You win this round!")
            wins += 1
        else:
            print("You lose this round.")

    overall_score["rps"] += wins
    print(f"Total wins: {wins}")

# ---------------------- Function 3: Trivia Game ----------------------
def trivia_game():
    print("\n--- Trivia Pursuit ---")
    questions = [
        {"question": "Which country has the highest life expectancy?", "options": ["A. Monaco", "B. Hong Kong", "C. Japan"], "answer": "A"},
        {"question": "How many faces does a Dodecahedron have?", "options": ["A. 24", "B.14", "C. 12"], "answer": "C"},
        {"question": "Who is the first female president of Bhutan?", "options": ["A. Ngawang Choden", "B. Dorji Choden", "C. Tshering Choden"], "answer": "B"}
    ]
    score = 0
    for q in questions:
        print(q["question"])
        for opt in q["options"]:
            print(opt)
        ans = input("Your answer (A/B/C): ").upper()
        if ans == q["answer"]:
            print("Correct!")
            score += 1
        else:
            print("Wrong!")
    overall_score["trivia"] += score
    print(f"Trivia score: {score}")

# ---------------------- Function 4: Pokemon Binder Manager ----------------------
def add_pokemon_card():
    try:
        pokedex_number = int(input("Enter Pokedex number (1–1025): "))
        if pokedex_number < 1 or pokedex_number > MAX_POKEDEX:
            print("Invalid Pokedex number.")
            return
        if pokedex_number in binder:
            print("Card already exists in the binder.")
            return

        page = (pokedex_number - 1) // CARDS_PER_PAGE + 1
        index = (pokedex_number - 1) % CARDS_PER_PAGE
        row = index // COLUMNS + 1
        col = index % COLUMNS + 1

        binder[pokedex_number] = (page, row, col)
        print(f"Page: {page}")
        print(f"Position: Row {row}, Column {col}")
        print(f"Status: Added Pokedex #{pokedex_number} to binder")
        overall_score["pokemon"] = len(binder)

        if len(binder) == MAX_POKEDEX:
            print("You have caught them all!!")

    except ValueError:
        print("Invalid input.")

def reset_binder():
    print("WARNING: This will delete ALL Pokemon cards from the binder.")
    confirm = input("Type 'CONFIRM' to reset or 'EXIT' to return: ")
    if confirm == "CONFIRM":
        binder.clear()
        overall_score["pokemon"] = 0
        print("The binder reset was successful!")
    else:
        print("Reset canceled.")

def view_binder():
    print("\n--- Current Binder Contents ---")
    if not binder:
        print("The binder is empty.")
    else:
        for num in sorted(binder):
            page, row, col = binder[num]
            print(f"Pokedex #{num} - Page {page}, Position: Row {row}, Column {col}")
    total = len(binder)
    percent = (total / MAX_POKEDEX) * 100
    print(f"Total cards: {total}")
    print(f"Completion: {percent:.1f}%")

def pokemon_binder_manager():
    while True:
        print("\nPokemon Card Binder Manager")
        print("1. Add Pokemon card")
        print("2. Reset binder")
        print("3. View current placements")
        print("4. Exit")
        choice = input("Select option: ")
        if choice == "1":
            add_pokemon_card()
        elif choice == "2":
            reset_binder()
        elif choice == "3":
            view_binder()
        elif choice == "4":
            print("Thank you for using the Pokemon Card Binder Manager!")
            break
        else:
            print("Invalid option.")

# ---------------------- Function 5: Overall Score ----------------------
def show_score():
    print("\n--- Overall Score ---")
    for game, score in overall_score.items():
        print(f"{game.replace('_', ' ').title()}: {score}")

# ---------------------- Main Program ----------------------
def main():
    while True:
        print("\nMain Menu")
        print("1. Guess Number Game")
        print("2. Rock Paper Scissors")
        print("3. Trivia Pursuit Game")
        print("4. Pokemon Card Binder Manager")
        print("5. Check Current Overall Score")
        print("0. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            guess_number_game()
        elif choice == "2":
            rock_paper_scissors()
        elif choice == "3":
            trivia_game()
        elif choice == "4":
            pokemon_binder_manager()
        elif choice == "5":
            show_score()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 0 to 5.")

if __name__ == "__main__":
    main()