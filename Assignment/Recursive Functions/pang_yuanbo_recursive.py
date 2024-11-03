#Yuanbo Pang
#This program uses recursive functions to display consecutive integers and calculate their sum.
def display_em(lower, upper):
    """ This recursive function displays the consecutive integers
    from its lower to its upper bounds """
    if lower > upper:
        return
    else:
        print(lower)
        display_em(lower + 1, upper)


def add_em(lower, upper):
    """ This recursive function calculates the sum of the consecutive
    integers from its lower to its upper bounds """
    if lower > upper:
        return 0
    else:
        return lower + add_em(lower + 1, upper)


def applyToEach(f, lower_bound, upper_bound):
    """ This higher-order function applies the included function
    to its lower and upper bound arguments"""
    return f(lower_bound, upper_bound)



if __name__ == "__main__":
    lower = int(input("Enter a lower bound: "))
    upper = int(input("Enter an upper bound: "))

    print("\nThe consecutive integers:")
    applyToEach(display_em, lower, upper)

    result = applyToEach(add_em, lower, upper)
    print(f"\nAdd up to {result}")
