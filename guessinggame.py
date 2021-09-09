import random


def main():
    show_header()

def show_header():
    print("-----------------------")
    print("    Guessing Game!")
    print("-----------------------")


def data_get():
    ammo_count = random.randint(1, 100)
    attempt_limit = 5
    attempts = 0
    print("Guess the number of bullets and get a free mag!")
    print()


def input_get(attempts, attempt_limit, ammo_count):
    while attempts < attempt_limit:
        guess_text = input("How many bullets are in the box? ")
        guess = int(guess_text)
        attempts += 1

        if guess == ammo_count:
            print(f"Correct! It was {guess}")
            exit()
        elif guess < ammo_count:
            print("Sorry, that's too low!")
        else:
            print("Sorry, that's too high!")

    print(f"Nope! The answer was {ammo_count}")


if __name__ == '__main__':
    main()
