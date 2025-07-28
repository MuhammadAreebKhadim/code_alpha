def chatbot():
    print("🤖 Chatbot is online! (type 'bye' to exit)")

    while True:
        user = input("👤 You: ").lower()

        if "hello" in user or "hi" in user:
            print("🤖 Bot: Hi there! 👋")
        elif "how are you" in user:
            print("🤖 Bot: I'm doing great, thanks! How about you?")
        elif "i'm fine" in user or "i am fine" in user:
            print("🤖 Bot: Glad to hear that! 😊")
        elif "what's your name" in user or "your name" in user:
            print("🤖 Bot: I'm PyBot, your Python-powered assistant! 🤓")
        elif "what can you do" in user:
            print("🤖 Bot: I can chat with you, tell jokes, and keep you company! 🧠💬")
        elif "tell me a joke" in user or "joke" in user:
            print("😂 Bot: Why did the programmer quit his job? Because he didn't get arrays! 😆")
        elif "thanks" in user or "thank you" in user:
            print("🤖 Bot: You're welcome! 🙌")
        elif "bye" in user or "goodbye" in user:
            print("👋 Bot: Goodbye! Have a nice day!")
            break
        else:
            print("❓ Bot: Sorry, I didn't understand that. Try asking something else!")

chatbot()
