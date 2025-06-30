def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return 'Error: Too many problems.'

    top_rows = []
    bottom_rows = []
    dashes = []
    answers = []
    problem_widths = []  # Initialize a list to store widths for answers

    for problem in problems:
        parts = problem.split()
        if len(parts) != 3:
            return 'Error: Invalid problem format.'

        num1, operator, num2 = parts

        if operator not in ('+', '-'):
            return 'Error: Operator must be \'+\' or \'-\'.'

        if not (num1.isdigit() and num2.isdigit()):
            return 'Error: Numbers must only contain digits.'

        if len(num1) > 4 or len(num2) > 4:
            return 'Error: Numbers cannot be more than four digits.'

        # Calculate the width for this problem
        max_length = max(len(num1), len(num2)) + 2  # +2 for operator and space
        problem_widths.append(max_length)  # Store the width for later use

        # Format the numbers and operator
        top_rows.append(num1.rjust(max_length))
        bottom_rows.append(operator + ' ' + num2.rjust(max_length - 2))
        dashes.append('-' * max_length)

        # Calculate the answer if needed
        if show_answers:
            if operator == '+':
                answer = str(int(num1) + int(num2))
            else:
                answer = str(int(num1) - int(num2))
            answers.append(answer)

    # Join the rows with four spaces
    arranged_problems = '    '.join(top_rows) + '\n' + \
                        '    '.join(bottom_rows) + '\n' + \
                        '    '.join(dashes)

    # Add answers if required
    if show_answers and answers:
        answer_line = '    '.join(
            answer.rjust(width) 
            for answer, width in zip(answers, problem_widths)
        )
        arranged_problems += '\n' + answer_line

    return arranged_problems

# Test cases
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_arranger(["3801 - 2", "123 + 49"]))
print(arithmetic_arranger(["1 + 2", "1 - 9380"]))
print(arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_arranger(["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"]))
print(arithmetic_arranger(["44 + 815", "909 - 2", "45 + 43", "123 + 49", "888 + 40", "653 + 87"]))
print(arithmetic_arranger(["3 / 855", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_arranger(["24 + 85215", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_arranger(["98 + 3g5", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_arranger(["3 + 855", "988 + 40"], True))
print(arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"], True))

print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')
