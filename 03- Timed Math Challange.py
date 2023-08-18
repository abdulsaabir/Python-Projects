import random
import time

# Constants for the arithmetic quiz
OPERATORS = ["+", "-", "*"]
MIN_OPERAND = 3
MAX_OPERAND = 12
TOTAL_PROBLEMS = 10

def generate_problem():
    """Generate a random arithmetic problem."""
    left_operand = random.randint(MIN_OPERAND, MAX_OPERAND)
    right_operand = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)
    problem_expression = f"{left_operand} {operator} {right_operand}"
    answer = eval(problem_expression)
    return problem_expression, answer

# Initialize the wrong answers count
wrong_answers = 0

# Start the quiz
input("Press Enter to start the arithmetic quiz!")
print("----------------------")

start_time = time.time()

# Iterate through each problem
for i in range(TOTAL_PROBLEMS):
    problem_expr, correct_answer = generate_problem()
    
    # Prompt the user to solve the problem
    while True:
        user_guess = input(f"Problem #{i + 1}: {problem_expr} = ")
        
        # Check the user's answer
        if user_guess == str(correct_answer):
            print("Correct Answer")
            break
        print("Wrong Answer")
        wrong_answers += 1

end_time = time.time()
total_time = round(end_time - start_time, 2)

print("----------------------")
print(f"Congratulations! You finished in {total_time} seconds!")
print(f"Total wrong attempts: {wrong_answers}")
