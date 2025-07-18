# BotSays - A Rule-Based Chatbot
# Created by Suchismita Padhi for CodSoft AI Internship

print("🤖 Welcome to BotSays! Type 'exit' anytime to end the chat.\n")

while True:
    user = input("You: ").lower()

    if user == "exit":
        print("BotSays: Goodbye! Take care 😊")
        break
    elif "hello" in user or "hi" in user:
        print("BotSays: Hello! How can I assist you today?")
    elif "your name" in user or "who are you" in user:
        print("BotSays: I’m BotSays — a simple chatbot created by Suchismita!")
    elif "how are you" in user:
        print("BotSays: I’m functioning well. Thanks for asking!")
    elif "bye" in user:
        print("BotSays: Bye! Hope to chat with you again.")
    elif "help" in user:
        print("BotSays: You can say hello, ask who I am, or just chat!")
    else:
        print("BotSays: Sorry, I didn't understand that.")
