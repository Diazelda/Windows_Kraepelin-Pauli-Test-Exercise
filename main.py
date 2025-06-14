"""Kraepelin/Pauli test training application."""

import random
import time

def generate_question():
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)
    result = num1 + num2
    return num1, num2, result

def get_user_input():
    """Return the digits entered by the user."""
    return input().strip()

def main():
    score = 0
    total_time = 0
    while True:
        num1, num2, result = generate_question()
        print(f"What is {num1} + {num2}?")

        start_time = time.time()
        user_input = get_user_input()
        end_time = time.time()

        elapsed_time = end_time - start_time
        total_time += elapsed_time

        if int(user_input) == result % 10:
            score += 1
            print("Correct!")
        else:
            print("Incorrect!")
            break

    average_time = total_time / score if score > 0 else 0

    print(f"\nGame over! Your score is {score}.")
    print(f"Average time used: {average_time:.2f} seconds.")

if __name__ == "__main__":
    main()
