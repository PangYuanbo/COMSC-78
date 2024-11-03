# pang_yuanbo_license.py This program administers a multiple-choice test. The program prompts the student to enter
# their answers to twenty questions. The program then compares the student's answers to the correct answers and
# displays the number of correct and incorrect answers. If the student answers at least 15 questions correctly,
# the program displays a message indicating that the student passed the test. The program also displays the numbers
# of the questions that the student answered incorrectly.

# Store the correct answers in a list
correct_answers = ['A', 'C', 'A', 'A', 'D',
                   'B', 'C', 'A', 'C', 'B',
                   'A', 'D', 'C', 'A', 'D',
                   'C', 'B', 'B', 'D', 'A']

# Initialize an empty list for the student's answers
student_answers = []

# Prompt the student to enter their answers to each of the twenty questions
for i in range(20):
    answer = input(f"Enter your answer for question {i+1}: ").strip().upper()
    student_answers.append(answer)

# Compare the student's answers to the correct answers
correct_count = 0
incorrect_questions = []

for i in range(20):
    if student_answers[i] == correct_answers[i]:
        correct_count += 1
    else:
        incorrect_questions.append(i+1)  # question numbers are 1-based

incorrect_count = 20 - correct_count

# Display the results
print(f"Number of correct answers: {correct_count}")
print(f"Number of incorrect answers: {incorrect_count}")

if correct_count >= 15:
    print("You passed the test.")
else:
    print("You did not pass the test.")

if incorrect_questions:
    incorrect_questions_str = ', '.join(str(num) for num in incorrect_questions)
    print(f"Questions answered incorrectly: {incorrect_questions_str}")
