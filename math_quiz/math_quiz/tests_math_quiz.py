import unittest
from math_quiz import RandomInteger, RandomSign, EquationFormula

def check_sign(rand_sign):
    if rand_sign == '+' or '-' or '*':
        return True 
    else:
        return False
    
class TestMathGame(unittest.TestCase):

    def test_RandomInteger(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = RandomInteger(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_RandomSign(self):
         rand_sign = RandomSign()
         output=check_sign(rand_sign)
         self.assertTrue(output)

    def test_EquationFormula(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (10, 12, '+', '10 + 12', 22),
                (5, 2, '-', '5 - 2', 3),
                (-2, 2, '+', '-2 + 2', 0),
                (3, 3, '*', '3 * 3', 9),
                (5, -9, '+', '5 + -9', -4),
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                 problem, answer=EquationFormula(num1,num2,operator)
                 self.assertEqual(problem, expected_problem)
                 self.assertEqual(answer, expected_answer)
                

if __name__ == "__main__":
    unittest.main()
