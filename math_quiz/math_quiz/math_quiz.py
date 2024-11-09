import random
from typing import Tuple

def RandomInteger(min_num : int, max_num : int) -> int:
    """
    Outputs a random number between 2 given bound.

    Parameters
    ----------
    min_num : int
        An integer specifying at which position to start.
    max_num : int
        An integer specifying at which position to end.

    Returns
    -------
    int
        An integer number selected element from the specified range.

    Raises
    ------
    TypeError
        If the numbers are not integer.
    ValueError
        If the first number is not equal or smaller than the second number.
    Exceptions
        if any unexpected error occurred.

    Examples
    --------
    RandomInteger(1, 8)
    3

    RandomInteger(16, 25)
    20
    """

    try:
        output = random.randint(min_num, max_num)
        return output
    except TypeError:
        # Handeling errors when the numbers are not integer.
        print("Numbers should be integer.")
        
    except ValueError:
        # Handeling errors when the numbers are not of the same bound.
        print("First number should be equal or smaller than the second number.")
    except Exception as e:
        # Catching any other exceptions.
        print(f"An unexpected error occurred: {e}")

    


def RandomSign() -> str:
    """
    Returns a random mathamtical sign from '+' or '-' or '*'.

    Returns
    -------
    str
        An integer number selected element from the specified range.

    Examples
    --------
    RandomSign()
    '+'

    RandomSign()
    '*'
    """
    #randomly choosing from '+' or '-' or '*'.
    return random.choice(['+', '-', '*'])


def EquationFormula(first_num : int, second_num : int, sign : str) -> Tuple[str, int]:
    """
    Outputs an equation formula and its result.

    Parameters
    ----------
    first_num : int
        An integer number.
    second_num : int
        An integer number.
    sign : str
        A mathmatical sign.

    Returns
    -------
    str
        An equation formulated from the inputs.
    int
        the output of the equation formulated.

    Raises
    ------
    Exceptions
        if any unexpected error occurred.

    Examples
    --------
    EquationFormula(1, 8, '+')
    '1 + 8', 9

    EquationFormula(2, 4, '*' )
    '2 * 4', 8
    """
    try :
        equation = f"{first_num} {sign} {second_num}" # the formulated equation from the inputs
        #the mathamtical operations are calculated based on the recieved mathmatical sign.
        if sign == '+': result = first_num + second_num 
        elif sign == '-': result = first_num - second_num
        else: result = first_num * second_num
        return equation, result
    except Exception as e:
        # Catching any other exceptions.
        print(f"An unexpected error occurred in EquationFormula : {e}")

def math_quiz():
    """
    It gives the user math equations and waits for their answer,
    if it is correct then a point is added.
    Raises
    ------
    Exceptions
        if any unexpected error occurred, the game will be over.

    """
    points = 0
    total_loops = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_loops):
        first_num = RandomInteger(1, 10); second_num = RandomInteger(1, 5); sign = RandomSign()

        try:
            PROBLEM, ANSWER = EquationFormula(first_num, second_num, sign)
            print(f"\nQuestion: {PROBLEM}")
            useranswer = input("Your answer: ")
            useranswer = int(useranswer)

            if useranswer == ANSWER:
                print("Correct! You earned a point.")
                points += -(-1)
            else:
                print(f"Wrong answer. The correct answer is {ANSWER}.")
        except Exception as e:
            # Catching any other exceptions.
            print(f"An unexpected error occurred in math_quiz : {e}")
        

    print(f"\nGame over! Your score is: {points}/{total_loops}")

if __name__ == "__main__":
    math_quiz()
