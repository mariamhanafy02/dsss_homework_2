import unittest
from math_quiz import RandomInt, RandomSign, CreatedEquation

def is_sign(sign):
    if sign == '+' or '-' or '*':
         return True
    else:
         return False
class TestMathGame(unittest.TestCase):

    def test_RandomInt(self):
        # Test if random numbers generated are within the specified range
        # min_val = 10
        # max_val = 9
        # for _ in range(1000):  # Test a large number of random values
        #     rand_num = RandomInt(min_val, max_val)
        #     self.assertTrue(min_val <= rand_num <= max_val)

        test_cases = [
                (1,10),(10, 2),(12.3,23)]

        for min_val, max_val in test_cases:
            rand_num = RandomInt(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_RandomSign(self):
        rand_sign = RandomSign()
        self.assertEqual(is_sign(rand_sign), True)

    def test_CreatedEquation(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),(10, 2, '+', '10 + 2', 12)]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                problem, answer = CreatedEquation(num1,num2,operator)
                self.assertEqual(problem, expected_problem)
                self.assertEqual(answer, expected_answer)

if __name__ == "__main__":
    unittest.main()
