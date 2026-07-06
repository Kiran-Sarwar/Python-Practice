import random

while True:
    print("\n=== Number Guessing Game ===")

    # Choose difficulty
    print("Select Difficulty:")
    print("1. Easy (1-50)")
    print("2. Medium (1-100)")
    print("3. Hard (1-200)")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        max_number = 50
    elif choice == "2":
        max_number = 100
    elif choice == "3":
        max_number = 200
    else:
        print("Invalid choice. Defaulting to Medium.")
        max_number = 100

    secret_number = random.randint(1, max_number)
    max_attempts = 10
    attempts = 0

    print(f"\nI'm thinking of a number between 1 and {max_number}.")
    print(f"You have {max_attempts} attempts.")

    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < secret_number:
                print("Too low!")
            elif guess > secret_number:
                print("Too high!")
            else:
                print("Correct!")
                print(f"You guessed the number in {attempts} attempts!")
                break

            print(f"Attempts remaining: {max_attempts - attempts}")

        except ValueError:
            print("Please enter a valid number.")

    else:
        print(f"\nGame Over! You ran out of attempts.")
        print(f"The correct number was {secret_number}.")

    play_again = input("\nDo you want to play again? (yes/no): ").lower()

    if play_again != "yes":
        print("Thanks for playing! Goodbye!")
        break