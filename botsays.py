# BotSays - A Rule-Based Chatbot
# Created by Suchismita Padhi for CodSoft AI Internship

import re
import random

print("BotSays: Hello! I'm BotSays, your smart chatbot. Ask me anything! Type 'bye' to exit.")

# === Motivational quotes, jokes, and language greetings ===
quotes = [
    "Push yourself, because no one else is going to do it for you.",
    "Dream big and dare to fail.",
    "Success doesn’t come to you. You go to it."
]

jokes = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "Why was the math book sad? Because it had too many problems.",
    "What do you call fake spaghetti? An impasta!"
]

language_greetings = {
    "hindi": "नमस्ते! मैं आपकी कैसे मदद कर सकती हूँ?",
    "odia": "ନମସ୍କାର! ମୁଁ ଆପଣଙ୍କୁ କିପରି ସହଯୋଗ କରିପାରିବି?",
    "spanish": "¡Hola! ¿Cómo puedo ayudarte?",
    "french": "Bonjour! Comment puis-je vous aider?"
}

# === Subject-specific facts ===
science_facts = {
    "sun": "The Sun is a star at the center of our solar system.",
    "gravity": "Gravity is a force that pulls objects toward each other.",
    "human body": "The human body has 206 bones."
}

english_tips = {
    "noun": "A noun is a word that names a person, place, or thing.",
    "verb": "A verb shows action or a state of being.",
    "idiom": "‘Break the ice’ means to start a conversation in a social setting."
}

gk_answers = {
    "capital of india": "The capital of India is New Delhi.",
    "largest ocean": "The Pacific Ocean is the largest ocean in the world.",
    "first president of india": "Dr. Rajendra Prasad was the first President of India."
}

# === Evaluate math expression ===
def solve_math(question):
    try:
        expression = re.findall(r'[0-9\+\-\*/\.\s]+', question)[0]
        result = eval(expression)
        return f"The answer is {result}"
    except:
        return "I couldn’t understand the math expression properly."

# === Python quiz mode ===
def start_quiz():
    questions = [
        {"q": "What does 'len()' do in Python?", "a": "B", "opt": ["A) Adds numbers", "B) Returns length", "C) Exits loop", "D) Declares variable"]},
        {"q": "What is the output of 5//2?", "a": "C", "opt": ["A) 2.5", "B) 2.0", "C) 2", "D) 3"]},
        {"q": "Which is a correct variable name?", "a": "A", "opt": ["A) my_var", "B) 2var", "C) my-var", "D) var name"]},
    ]
    score = 0
    for i, q in enumerate(questions):
        print(f"\nQ{i+1}: {q['q']}")
        for o in q["opt"]:
            print(o)
        ans = input("Your answer (A/B/C/D): ").upper()
        if ans == q["a"]:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong. Correct answer is {q['a']}")
    print(f"\nYou scored {score}/{len(questions)}")

# === Main Chat Loop ===
while True:
    user = input("You: ").lower()

    if user in ["bye", "exit", "quit"]:
        print("BotSays: Goodbye! Come back soon 😊")
        break

    elif "how are you" in user:
        print("BotSays: I'm doing great! How about you?")

    elif "your name" in user:
        print("BotSays: I’m BotSays, built to assist you with cool facts and fun talk!")

    elif "joke" in user:
        print("BotSays:", random.choice(jokes))

    elif "motivate" in user:
        print("BotSays:", random.choice(quotes))

    elif "thank" in user:
        print("BotSays: You're welcome!")

    elif "quiz" in user:
        start_quiz()

    elif any(op in user for op in ['+', '-', '*', '/']):
        print("BotSays:", solve_math(user))

    elif any(word in user for word in science_facts):
        for key in science_facts:
            if key in user:
                print("BotSays:", science_facts[key])
                break

    elif any(word in user for word in english_tips):
        for key in english_tips:
            if key in user:
                print("BotSays:", english_tips[key])
                break

    elif any(word in user for word in gk_answers):
        for key in gk_answers:
            if key in user:
                print("BotSays:", gk_answers[key])
                break

    elif any(lang in user for lang in language_greetings):
        for lang in language_greetings:
            if lang in user:
                print("BotSays:", language_greetings[lang])
                break

    elif "help" in user:
        print("BotSays: You can ask me questions about science, English, math, general knowledge, or just chat!")

    else:
        print("BotSays: Hmm... I'm still learning. Can you try asking differently?")

