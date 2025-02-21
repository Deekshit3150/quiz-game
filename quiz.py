import random
import time

# Quiz Questions Database
quiz_questions = {
    "easy": [
        {"question": "What is the capital of France?", "options": ["A) Berlin", "B) Madrid", "C) Paris", "D) Rome"], "answer": "C"},
        {"question": "How many legs does a spider have?", "options": ["A) 6", "B) 8", "C) 10", "D) 12"], "answer": "B"},
        {"question": "What is 5 + 3?", "options": ["A) 6", "B) 7", "C) 8", "D) 9"], "answer": "C"},
        {"question": "Which planet is known as the Red Planet?", "options": ["A) Venus", "B) Mars", "C) Jupiter", "D) Saturn"], "answer": "B"},
        {"question": "What color is a banana?", "options": ["A) Red", "B) Blue", "C) Yellow", "D) Green"], "answer": "C"}
    ],
    "medium": [
        {"question": "What is the largest planet in our solar system?", "options": ["A) Mars", "B) Earth", "C) Jupiter", "D) Saturn"], "answer": "C"},
        {"question": "Who developed the theory of relativity?", "options": ["A) Isaac Newton", "B) Albert Einstein", "C) Galileo Galilei", "D) Nikola Tesla"], "answer": "B"},
        {"question": "What is the square root of 144?", "options": ["A) 10", "B) 11", "C) 12", "D) 13"], "answer": "C"},
        {"question": "Which continent is known as the ‘Dark Continent’?", "options": ["A) Asia", "B) South America", "C) Africa", "D) Antarctica"], "answer": "C"},
        {"question": "Which is the longest river in the world?", "options": ["A) Amazon River", "B) Nile River", "C) Yangtze River", "D) Mississippi River"], "answer": "B"}
    ],
    "hard": [
        {"question": "What is the chemical symbol for gold?", "options": ["A) Au", "B) Ag", "C) Pb", "D) Fe"], "answer": "A"},
        {"question": "Which element has the atomic number 1?", "options": ["A) Oxygen", "B) Helium", "C) Hydrogen", "D) Nitrogen"], "answer": "C"},
        {"question": "Who painted the ceiling of the Sistine Chapel?", "options": ["A) Leonardo da Vinci", "B) Michelangelo", "C) Raphael", "D) Donatello"], "answer": "B"},
        {"question": "What is the powerhouse of the cell?", "options": ["A) Nucleus", "B) Ribosome", "C) Mitochondria", "D) Golgi apparatus"], "answer": "C"},
        {"question": "Which scientist discovered penicillin?", "options": ["A) Marie Curie", "B) Alexander Fleming", "C) Louis Pasteur", "D) Joseph Lister"], "answer": "B"}
    ]
}

leaderboard = []  # Store high scores

def calculate_iq_level(score, max_score):
    """Determines IQ level based on score percentage."""
    percentage = (score / max_score) * 100
    if percentage == 100:
        return "Genius IQ 🤯"
    elif percentage >= 80:
        return "Very High IQ 🔥"
    elif percentage >= 60:
        return "Above Average IQ 👍"
    elif percentage >= 40:
        return "Average IQ 🙂"
    else:
        return "Below Average IQ 😕"

def start_quiz():
    """Starts the quiz game with a timer, lifelines, and progress tracking."""
    print("🎯 Welcome to the Quiz Game!")
    player_name = input("Enter your name: ")

    level = input("Choose a difficulty level (easy, medium, hard): ").lower()
    if level not in quiz_questions:
        print("Invalid choice. Please select easy, medium, or hard.")
        return

    questions = random.sample(quiz_questions[level], min(5, len(quiz_questions[level])))
    score = 0
    max_score = len(questions) * 10
    lifelines = {"50-50": True, "Skip": True}  # Lifelines

    for index, q in enumerate(questions):
        print(f"\n🔹 Question {index + 1}/{len(questions)}:")
        print(q["question"])
        for option in q["options"]:
            print(option)

        print("\n💡 Lifelines available:", ", ".join([k for k, v in lifelines.items() if v]))
        start_time = time.time()

        answer = input("Enter your answer (A, B, C, or D) or type '50-50' or 'Skip': ").upper()
        elapsed_time = time.time() - start_time

        if elapsed_time > 10:
            print("⏳ Time's up! You missed this question.")
            continue  # Skip to next question

        if answer == "50-50" and lifelines["50-50"]:
            lifelines["50-50"] = False
            correct_option = q["answer"]
            remaining_options = [correct_option] + random.sample([opt[0] for opt in q["options"] if opt[0] != correct_option], 1)
            print(f"50-50 Lifeline used! Remaining options: {remaining_options}")
            answer = input("Enter your answer (A or B): ").upper()

        if answer == "SKIP" and lifelines["Skip"]:
            lifelines["Skip"] = False
            print("⏭️ Skipped this question!")
            continue

        if answer == q["answer"]:
            print("✅ Correct!")
            score += 10
        else:
            print(f"❌ Wrong! The correct answer was {q['answer']}.")

        print(f"📊 Progress: {index + 1}/{len(questions)} questions completed.")

    iq_level = calculate_iq_level(score, max_score)
    leaderboard.append({"name": player_name, "score": score})

    print(f"\n🏆 {player_name}, your final score: {score}/{max_score} points")
    print(f"🧠 IQ Level: {iq_level}")

    # Show leaderboard
    print("\n🎖️ Leaderboard:")
    sorted_leaderboard = sorted(leaderboard, key=lambda x: x["score"], reverse=True)
    for idx, entry in enumerate(sorted_leaderboard[:5]):
        print(f"{idx + 1}. {entry['name']} - {entry['score']} points")

    print("🎉 Thanks for playing!")

# Run the quiz
start_quiz()
