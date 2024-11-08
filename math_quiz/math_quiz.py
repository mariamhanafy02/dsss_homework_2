import random


def RandomInt(min_number: int, max_number: int) -> int:
    """
    Gives a random integer between the given numbers.

    parameters 

    --------------
    min_number : int 
                the minimum integer to start randomizing from

    max_number : int 
                the maximum integer to end randomizing to


    Returns
    --------
    int 
        the random number between 'min_number' and 'max_number'


    Exampels 
    --------

    >>>>RandomInt(8, 15)
    9

    """
    #error handeling for non integer numbers 

    # if not isinstance(min_number,int):
    #     raise TypeError('Minumim number should be int')
    # if not isinstance(max_number,int):   
    #     raise TypeError('Maximum number should be int')
    try :
        random_number=random.randint(min_number, max_number) # randomizing between 2 given integer numbers
    except TypeError:
        print('numbers should be int')
    except ValueError:
        print('numbers should have a bound in between')
   
    
    return random_number


def RandomSign() -> str :
    """
    chooses a random mathmatical sign from '+', '-', '*'.

    Returns
    --------
    str 
        a random sign between from '+', '-', '*'.
    Exampels 
    --------

    >>>>RandomSign()
    '+'

    """
    math_sign= random.choice(['+', '-', '*']) #choosing between mathmatical signs
    return math_sign


def CreatedEquation(first_number : int, second_number :int, sign : str) -> tuple[str,int] :
    """
    creates an equation from 2 given numbers and a mathmatical sign.
    
    parameters 

    --------------
    first_number : int 
                an integer number

    second_number : int 
                an integer number
    sign : str 
                a mathmatical sign

    Returns
    --------
    str 
        the mathmatical equation in a string type.

    int 
        the output of the equation.
    Exampels 
    --------

    >>>>CreatedEquation(1,2,'+')
    '1 + 2' , 3

    """
    equation = f"{first_number} {sign} {second_number}" # creates the equation into a string
    if sign == '-': output = first_number - second_number
    elif sign == '+': output = first_number + second_number
    else: output = first_number * second_number
    return equation, output

def math_quiz():
    """
    the function randomizes 2 numbers and a mathmatical sign as well, creates an equation from these numbers and waits 
    for the user input, for every correct answer, it adds points.

    """
    points = 0
    total_loops = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_loops):
        first_number = RandomInt(10, 13); second_number = RandomInt(1, 5.5); sign = RandomSign()

        PROBLEM, ANSWER = CreatedEquation(first_number, second_number, sign) # creating an equation from the random numbers and the mathmatical sign 
        print(f"\nQuestion: {PROBLEM}") # prints the problem to the user
        useranswer = input("Your answer: ") # waits for the user answer
        useranswer = int(useranswer) 

        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            points += -(-1) # if the user answer is the same as the solution of the equation it adds point to the user.
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {points}/{total_loops}")

if __name__ == "__main__":
    math_quiz()
