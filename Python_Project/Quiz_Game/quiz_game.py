import time
import random
questions = [
    {
        "question": "Which country recently held a summit with India to enhance defense cooperation under the Comprehensive Strategic Partnership?",
        "options": ["Russia", "France", "USA", "Australia"],
        "answer": "France"
    },
    {
        "question": "India signed a trade agreement with which regional economic bloc in 2024?",
        "options": ["ASEAN", "EU", "GCC", "African Union"],
        "answer": "EU"
    },
    {
        "question": "Which neighboring country recently resolved a long-standing border dispute with India?",
        "options": ["Nepal", "Bhutan", "Bangladesh", "Sri Lanka"],
        "answer": "Bangladesh"
    },
    {
        "question": "India and which country jointly launched the 'India-Middle East-Europe Economic Corridor' (IMEC)?",
        "options": ["Saudi Arabia", "UAE", "Israel", "Egypt"],
        "answer": "UAE"
    },
    {
        "question": "India recently participated in which major regional security dialogue aimed at ensuring stability in the Indo-Pacific?",
        "options": ["ASEAN Summit", "Quad Summit", "SAARC Summit", "G20 Summit"],
        "answer": "Quad Summit"
    }
]


def run_quiz(questions):
    score = 0
    random.shuffle(questions)

    print("Welcome to the Quiz Game!")
    print("You have 10 seconds for each question. Let's begin!\n")

    for index, q in enumerate(questions, 1):
        print(f"Question {index}: {q['question']}")
        random.shuffle(q['options'])  # Shuffle options for randomness

        for i, opt in enumerate(q['options'], 1):
            print(f"{chr(64+i)}. {opt}")
        
        start_time = time.time()
        answer = input("Enter your answer (A, B, C, or D): ").strip().upper()
        end_time = time.time()

        if end_time - start_time > 10:
            print("⏱ Time's up! Moving to the next question.\n")
        else:
            correct_option = chr(65 + q['options'].index(q['answer']))  
            if answer == correct_option:
                print("✅ Correct!\n")
                score += 1
            else:
                print(f"❌ Wrong! The correct answer was: {correct_option}. {q['answer']}\n")
    
    print(f"Quiz Over! Your Final Score: {score}/{len(questions)}")
    print("Thank you for playing!")

# Run the quiz
run_quiz(questions)
