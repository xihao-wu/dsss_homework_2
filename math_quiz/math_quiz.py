import random


def generate_random_number(min_value, max_value):
    """
    Generate a random integer between min_value and max_value.

    :param min_value: The minimum value of the range.
    :param max_value: The maximum value of the range.
    :return: Random integer between min_value and max_value.
    """
    return random.randint(min_value, max_value)


def choose_random_operator():
    """
    Randomly choose a math operator from +, -, or *.

    :return: A string representing a math operator.
    """
    return random.choice(['+', '-', '*'])


def create_math_problem(num1, num2, operator):
    """
    Create a math problem string and calculate its answer.

    :param num1: The first number in the math problem.
    :param num2: The second number in the math problem.
    :param operator: The operator of the math problem.
    :return: A tuple containing the math problem string and its answer.
    """
    problem = f"{num1} {operator} {num2}"
    if operator == '+':
        answer = num1 + num2
    elif operator == '-':
        answer = num1 - num2
    else:
        answer = num1 * num2
    return problem, answer


def math_quiz():
    """
    Run a math quiz game where the user solves math problems.
    """
    score = 0
    total_questions = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        num1 = generate_random_number(1, 10)
        num2 = generate_random_number(1, 10)  # Fixed to ensure it's always an integer
        operator = choose_random_operator()

        problem, correct_answer = create_math_problem(num1, num2, operator)
        print(f"\nQuestion: {problem}")
        try:
            user_answer = int(input("Your answer: "))
            if user_answer == correct_answer:
                print("Correct! You earned a point.")
                score += 1
            else:
                print(f"Wrong answer. The correct answer is {correct_answer}.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")


def main():
    math_quiz()  # Here we call the function that starts the game.

if __name__ == "__main__":
    main()
