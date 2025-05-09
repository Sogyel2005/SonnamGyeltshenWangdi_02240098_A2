# Function 4: Pokemon Binder Manager 
binder = {}

MAX_POKEDEX = 1025
CARDS_PER_PAGE = 64
ROWS = 8
COLUMNS = 8
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
      

        if len(binder) == MAX_POKEDEX:
            print("You have caught them all!!")

    except ValueError:
        print("Invalid input.")

def reset_binder():
    print("WARNING: This will delete ALL Pokemon cards from the binder.")
    confirm = input("Type 'CONFIRM' to reset or 'EXIT' to return: ")
    if confirm == "CONFIRM":
        binder.clear()
       
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