import os
import json
import openai

# Ensure the API key is set
openai.api_key = os.getenv('OPENAI_API_KEY')

def respond_to_query(query, config_file="customer_service_bot_config.json"):
    """Generate a response based on the website's FAQ and services."""
    try:
        with open(config_file, 'r') as file:
            config = json.load(file)
    except FileNotFoundError:
        return "Error: No bot configuration found. Please build the bot first."

    # Check FAQ for a direct match
    for question, answer in config['faq'].items():
        if query.lower() in question.lower():
            return answer

    # If no match, generate a response using OpenAI
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": f"You are a customer service bot for {config['website_name']}. Provide detailed, helpful responses."},
                {"role": "user", "content": query}
            ]
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"Error: {e}"
