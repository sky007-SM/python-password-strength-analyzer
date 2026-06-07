# Python Password Strength Analyzer

# Imported choice from secrects as choose to solve variable conflict with choice
from secrets import choice as choose
from typing import TypedDict
from random import choices, randint


# Explicit type hinting the flags used via a dictionary
class BooleanFlags(TypedDict):
    uppercase_character: bool
    lowercase_character: bool
    number: bool
    special_character: bool
    password_length: bool


# Boolean flags type and condition set types
type boolean_flags = BooleanFlags
type condition_set = list[list[str]]


# Function that defines valid sets of characters for strong password
def password_character_set() -> condition_set:
    uppercase_alphabets: list[str] = [chr(alpha) for alpha in range(65, 91)]
    lowercase_alphabets: list[str] = [chr(alpha) for alpha in range(97, 123)]
    numbers_list: list[str] = [str(num) for num in range(10)]
    special_characters: list[str] = [
        "!",
        "@",
        "#",
        "$",
        "%",
        "^",
        "&",
        "*",
        "(",
        ")",
        "_",
        "-",
        "+",
        "=",
    ]
    strong_character_set: condition_set = [
        uppercase_alphabets,
        lowercase_alphabets,
        numbers_list,
        special_characters,
    ]
    return strong_character_set


# Function that creates an assorted collection of index
def random_index_creator(password_length: int) -> list[int]:

    key_values: set[int] = {0, 1, 2, 3}

    # Instead of recursion used while True for removing sublayers
    while True:
        # Choices used from random function
        random_index_set: list[int] = choices(
            [0, 1, 2, 3], weights=(2, 3, 1, 1), k=password_length
        )
        if key_values.issubset(set(random_index_set)):
            return random_index_set  # It is essential to have return to exit loop


# Function that generates random strong password
def password_generator(strong_character_set: condition_set) -> None:
    password_length: int = randint(8, 25)
    random_index_set: list[int] = random_index_creator(
        password_length
    )  # Invokes random_index creator function

    # Uses choice from secrets as choose
    password_characters: list[str] = [
        choose(strong_character_set[index]) for index in random_index_set
    ]

    password: str = "".join(
        password_characters
    )  # Join method used since its better than concatenation

    print(f"\nStrong password generated: {password}")


# Function that provides initial instruction to user on ensuring password strength
def instruction_provider() -> str:
    print(f"\n======= Password Strength Checker =======")
    print(f"\nPassword must contain:")
    print(f"  - Minimum 8 character")
    print(f"  - An uppercase alphabet\n  - A lowercase alphabet")
    print(f"  - A number\n  - A special character")
    user_password: str = input("Enter your password: ")
    return user_password


# Function that checks whether password satisfies all conditions
def strength_evaluator(
    user_password: str, strong_character_set: condition_set
) -> boolean_flags:
    password_length: int = len(user_password)
    password_length_match: bool = False
    uppercase_present: bool = False
    lowercase_present: bool = False
    number_present: bool = False
    if password_length >= 8:
        password_length_match = True
    special_character_present: bool = False
    special_chars: set[str] = set(
        strong_character_set[3]
    )  # Better memory management with single initialization of set
    for index in range(password_length):
        if user_password[index].isupper():
            uppercase_present = True
        if user_password[index].islower():
            lowercase_present = True
        if user_password[index].isdigit():
            number_present = True
        if user_password[index] in special_chars:
            special_character_present = True

    # Converting boolean flags to dictionary to export
    password_strength_flags: boolean_flags = {
        "uppercase_character": uppercase_present,
        "lowercase_character": lowercase_present,
        "number": number_present,
        "special_character": special_character_present,
        "password_length": password_length_match,
    }
    return password_strength_flags


# Function that provides summary of analysis
def strength_summarizer(password_strength_flags: boolean_flags) -> None:
    password_strength: int = 0
    password_improvement_msg: list[str] = ["\nImprove Password by:"]
    print(f"\n====== Password Strength Analysis ======\n")
    if password_strength_flags["password_length"]:
        print("✓ Length Requirement Met")
        password_strength += 1
    else:
        print("✗ Length Requirement Not Met")
        password_improvement_msg.append("\n  -Increase number of characters")

    if password_strength_flags["uppercase_character"]:
        print("✓ Uppercase Alphabet Found")
        password_strength += 1
    else:
        print("✗ Uppercase Alphabet Missing")
        password_improvement_msg.append("\n  -Add uppercase letters")

    if password_strength_flags["lowercase_character"]:
        print("✓ Lowercase Alphabet Found")
        password_strength += 1
    else:
        print("✗ Lowercase Alphabet Missing")
        password_improvement_msg.append("\n  -Add lowercase letters")

    if password_strength_flags["number"]:
        print("✓ Number Character Found")
        password_strength += 1
    else:
        print("✗ Number Character Missing")
        password_improvement_msg.append("\n  -Add numbers")

    if password_strength_flags["special_character"]:
        print("✓ Special Character Found")
        password_strength += 1
    else:
        print("✗ Special Character Missing")
        password_improvement_msg.append("\n  -Add special characters")
    improvement_msg: str = "".join(
        password_improvement_msg
    )  # Join method used since its better than concatenation

    strength_rating(password_strength)  # Invokes the strength_rating function
    if password_strength < 5:
        print(improvement_msg)


# Function that provides score metrics
def strength_rating(password_strength: int) -> None:
    if password_strength < 2:
        print(f"\nOverall Strength: Weak")
    elif password_strength <= 4:
        print(f"\nOverall Strength: Medium")
    elif password_strength == 5:
        print(f"\nOverall Strength: Strong")


# Function that displays program as a menu app
def password_app_menu() -> None:

    # Instead of recursion used while True for removing sublayers
    while True:
        print("1. Generate Password\n2. Analyze Password Strength\n\n\n\t Quit - q")
        choice: str = (input("Enter your choice (1,2, or q): ")).lower()

        while choice not in ["1", "2", "q"]:  # Handles Invalid choice input
            print("\nInvalid choice entry")
            choice = input("Enter your choice (1,2, or q): ")
        if choice == "1":
            password_generator(password_character_set())  # Invokes password generator

        elif choice == "2":
            strength_summarizer(
                strength_evaluator(instruction_provider(), password_character_set())
            )  # Invokes the password strength analyzer
        elif choice == "q":
            break

        print(f"\nReturn to Menu -r\t\t2. Quit -q ")
        action: str = (input("Enter your choice (r/q): ")).lower()
        while action not in ["r", "q"]:  # Handles Invalid choice input
            print("\nInvalid choice entry")
            action = input("Enter your choice (r/q): ")

        if action == "q":
            break


# The main function
def main() -> None:
    print("======= Password Manager App ======= \n")
    password_app_menu()  # Invokes menu function


if __name__ == "__main__":
    main()
