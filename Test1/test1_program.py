#Yuanbo Pang
# Description: This program generates 100 random numbers between 1 and 1000 and counts how many of them are even and odd.
# The program then prints the results and asks the user if they would like to run the program again.
# The program will continue to run until the user chooses to exit.
# Import the random module to generate random numbers
import random


# Define a function to check if a number is even
def is_even(number):
    # If the number is divisible by 2, return True, otherwise return False
    return number % 2 == 0


# Outer loop to allow repeated execution of the program
while True:
    # Initialize counters for even and odd numbers
    odd_count = 0
    even_count = 0

    # Loop to generate 100 random numbers between 1 and 1000
    for _ in range(100):
        # Generate a random integer between 1 and 1000
        currentNumber = random.randint(1, 1000)

        # Check if the number is even using the is_even function
        if is_even(currentNumber):
            # Increment the even number counter
            even_count += 1
        else:
            # Increment the odd number counter
            odd_count += 1

    # print the results
    print(f"Out of 100 random numbers, {odd_count} were odd, and {even_count} were even.")

    # Ask the user if they want to run the program again and change it to lowercase
    repeat = input("Would you like to run the program again (Y/N): ").lower()

    # If the user inputs 'n', break the loop and exit the program
    if repeat != 'y':
        break
