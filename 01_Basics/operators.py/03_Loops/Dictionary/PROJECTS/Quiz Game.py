questions = {
    "What is the capital of India?": "delhi",
    "What is 10 + 5?": "15",
    "Which language are we learning?": "python",
    "How many days are there in a week?": "7",
    "What is 5 * 5?": "25"
}

score = 0

for question, answer in questions.items():

    user_answer = input(question + " ").lower()

    if user_answer == answer:
        print("Correct! ✅")
        score = score + 1
    else:
        print("Wrong! ❌")
        print("Correct Answer:", answer)

    print("-------------------------")

print("\n========== QUIZ RESULT ==========")
print("Total Questions:", len(questions))
print("Correct Answers:", score)
print("Wrong Answers:", len(questions) - score)

percentage = (score / len(questions)) * 100

print("Score Percentage:", percentage, "%")

if percentage >= 80:
    print("Excellent Performance! 🏆")
elif percentage >= 60:
    print("Very Good! 🔥")
elif percentage >= 40:
    print("Good, Keep Practicing!")
else:
    print("Need More Practice! 💪")