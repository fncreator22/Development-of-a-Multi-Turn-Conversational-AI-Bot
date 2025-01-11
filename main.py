from conversation import handle_conversation

if __name__ == "__main__":
    print("Chat with the bot! Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        response = handle_conversation(user_input)
        print(f"Bot: {response}")
