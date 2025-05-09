# Global variables
import random
import SonamGyeltshenWangdi_02240098_A2_PB
overall_score = {
    "guess_number": 0,
    "rps": 0,
    "trivia": 0,
    "pokemon": 0
}

# Function 1: Guess the Number game 
def guess_number_game():
    secret_number = random.randint(1, 100)
    print("I'm thinking of a number between 1 and 100.")
    
    attempts = 0
    while True:
        try:
            guess = int(input("Your guess: "))
            attempts += 1
            
            if guess == secret_number:
                print(f"Correct! You got it in {attempts} tries!")
                break
            elif guess < secret_number:
                print("Too low!")
            else:
                print("Too high!")
        except ValueError:
            print("Enter a valid number.")

    score = max(0, 10 - guess4)
    overall_score["guess_number"] += score
    print(f"Your score: {score}")

#  Function 2: Rock Paper Scissors 
def rock_paper_scissors():
    print("\n--- Rock Paper Scissors ---")
    options = ['rock', 'paper', 'scissors']
    wins = 0

    for round_num in range(3):
        computer = random.choice(options)
        user = input("Choose rock, paper,  scissors or quit : ").lower()
        if user == "quit":
            break
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
            break
        else:
            print("You lose this round.")

        

    overall_score["rps"] += wins
    print(f"Total wins: {wins}")
 

# Function 3: Trivia Game 
def trivia_game():
    print("\n--- Trivia Pursuit ---")
    questions = [
        {"question": "Which country has the highest life expectancy?", "options": ["A. Monaco", "B. Hong Kong", "C. Japan"], "answer": "A"},
        {"question": "How many faces does a Dodecahedron have?", "options": ["A. 24", "B.14", "C. 12"], "answer": "C"},
        {"question": "Who is the first female minister of Bhutan?", "options": ["A. Ngawang Choden", "B. Dorji Choden", "C. Tshering Choden"], "answer": "B"}
        
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


# Function 5: Overall Score 
def show_score():
    print("\n--- Overall Score ---")
    for game, score in overall_score.items():
        print(f"{game.replace('_', ' ').title()}: {score}")

#  Main Program 
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
            SonamGyeltshenWangdi_02240098_A2_PB.pokemon_binder_manager()
        elif choice == "5":
            show_score()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 0 to 5.")

if __name__ == "__main__":
    main()