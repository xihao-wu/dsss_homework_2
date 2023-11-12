import unittest
from math_quiz import generate_random_number, choose_random_operator, create_math_problem



class TestMathGame(unittest.TestCase):

    def test_generate_random_number(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = generate_random_number(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_choose_random_operator(self):
        # Test if the operator returned is one of the expected operators
        expected_operators = ['+', '-', '*']
        for _ in range(1000):  # Test a large number of times
            operator = choose_random_operator()
            self.assertIn(operator, expected_operators)

    def test_create_math_problem(self):
        # Test the creation of math problems and their solutions
        test_cases = [
            (5, 2, '+', '5 + 2', 7),
            (7, 3, '-', '7 - 3', 4),
            (5, 5, '*', '5 * 5', 25)
        ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            problem, answer = create_math_problem(num1, num2, operator)
            self.assertEqual(problem, expected_problem)
            self.assertEqual(answer, expected_answer)

if __name__ == "__main__":
    unittest.main()
