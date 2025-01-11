import os
import openai

openai.api_key = os.getenv('OPENAI_API_KEY')  # Ensure API key is set in .env


from bot_builder import gather_website_info

from customer_service_bot import respond_to_query

def main():
    print("Welcome! What would you like to do?")
    print("1. Build a new customer service bot")
    print("2. Interact with an existing customer service bot")
    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        gather_website_info()
    elif choice == "2":
        print("\nCustomer Service Bot ready. Type 'exit' to end the chat.")
        while True:
            user_input = input("You: ")
            if user_input.lower() == 'exit':
                print("Goodbye!")
                break
            bot_response = respond_to_query(user_input)
            print(f"Bot: {bot_response}")
    else:
        print("Invalid choice. Please restart the program.")

if __name__ == "__main__":
    main()
