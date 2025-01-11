import os
import json

def gather_website_info():
    """Collect information about the website from the user."""
    info = {}
    print("Welcome to the Bot Builder!")
    info['website_name'] = input("Enter the website name: ")
    info['website_url'] = input("Enter the website URL: ")
    info['services'] = input("List the main services offered by the website (comma-separated): ").split(',')
    info['faq'] = {}

    print("\nLet's create an FAQ section for the bot.")
    while True:
        question = input("Enter a FAQ question (or type 'done' to finish): ")
        if question.lower() == 'done':
            break
        answer = input("Enter the answer to this question: ")
        info['faq'][question] = answer

    save_bot_config(info)
    print("\nWebsite information collected successfully!")
    return info

def save_bot_config(config, file_name="customer_service_bot_config.json"):
    """Save the bot configuration to a JSON file."""
    with open(file_name, 'w') as file:
        json.dump(config, file, indent=4)

def load_bot_config(file_name="customer_service_bot_config.json"):
    """Load the bot configuration from a JSON file."""
    if not os.path.exists(file_name):
        return None
    with open(file_name, 'r') as file:
        return json.load(file)
