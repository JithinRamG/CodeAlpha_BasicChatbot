def chatbot():
    print("Hello! I'm a simple chatbot. Type 'bye' to exit anytime.")

    while True:
        user = input("You: ").lower()

        if user == "hello":
            print("Bot: Hi there!")
            
        elif user == "how are you":
            print("Bot: I'm fine,thanks!")

        elif user == "what is your name":
            print("Bot: I'm simple ChatBot!")

        elif user == "what can you do?":
            print("Bot: I can chat with you")

        elif user == "who created you?":
            print("Bot: I was created by Jithin!")

        elif user == "tell me a joke":
            print("Bot: Why do programmers prefer dark mode? Because light attracts bugs!")

        elif user == "bye":
            print("Bot: Goodbye!")

            break
        else:
            print("Bot: I didn't understand that.")
           
           
chatbot()