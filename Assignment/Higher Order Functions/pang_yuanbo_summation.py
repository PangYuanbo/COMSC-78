#Yuanbo Pang
# Define the higher-order summation function
def summation(f, lower, upper):
    """This function sums the values from the function f for each of the
    numbers between the lower and upper bounds, inclusive."""

    # revise and update the code from the summation function that was
    # introduced in section 1.6 of the text
    total = 0
    for i in range(lower, upper + 1):
        total += f(i)
    return total

# Define the square function
def square(x):
    """This function calculates and returns the square of the input argument x."""
    return x * x

# Define the fourth power function without using x**4, math.pow, or similar
def fourth_power(x):
    """ This function calculates and returns the fourth power of x.
    It uses neither x*x*x*x, x**4, nor math.pow(x, 4) """
    return square(square(x))  # Using square function to compute fourth power



lower_bound = int(input("Enter a lower bound for the sum: "))
upper_bound = int(input("Enter an upper bound for the sum: "))


sum_of_squares = summation(square, lower_bound, upper_bound)
print(f"The sum of squares of the numbers from {lower_bound} to {upper_bound} is {sum_of_squares}")


sum_of_fourth_powers = summation(fourth_power, lower_bound, upper_bound)
print(f"The sum of the fourth powers of the numbers from {lower_bound} to {upper_bound} is {sum_of_fourth_powers}")


sum_of_square_roots = summation(lambda x: x**0.5, lower_bound, upper_bound)
print(f"The sum of square roots of the numbers from {lower_bound} to {upper_bound} is {sum_of_square_roots}")
