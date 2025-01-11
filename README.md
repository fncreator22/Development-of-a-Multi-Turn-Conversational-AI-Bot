# 🤖 Multi-Turn Conversational AI Bot Using the Gemini API

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4-blue.svg)

Welcome to the Multi-Turn Conversational AI Bot project! This project leverages the power of OpenAI's GPT-4 model to create a customer service bot that can handle multi-turn conversations. The bot is designed to assist users with various queries related to the Split Money App.

## 🌟 Features

- **Multi-Turn Conversations**: The bot can handle complex, multi-turn conversations with users.
- **FAQ Integration**: The bot can answer frequently asked questions directly from a pre-defined FAQ list.
- **OpenAI GPT-4**: Utilizes OpenAI's GPT-4 model for generating responses.
- **Customizable**: Easily customizable to fit different websites and services.

## 📂 Project Structure
conversational_ai_bot/ ├── pycache/ ├── .env ├── api_caller.py ├── bot_builder.py ├── conversation.py ├── customer_service_bot_config.json ├── customer_service_bot.py ├── LICENSE ├── main.py ├── repository/ │ ├── file1.py │ └── file2.py ├── repository_handler.py └── requirements.txt


## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- OpenAI API Key

### Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/yourusername/conversational_ai_bot.git
    cd conversational_ai_bot
    ```

2. **Install dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

3. **Set up environment variables**:
    Create a [.env](http://_vscodecontentref_/10) file in the root directory and add your OpenAI API key:
    ```properties
    OPENAI_API_KEY=your_openai_api_key
    ```

### Usage

1. **Build a new customer service bot**:
    ```sh
    python conversation.py
    ```
    Follow the prompts to enter website information and FAQs.

2. **Interact with the bot**:
    ```sh
    python main.py
    ```
    Type your queries and get responses from the bot.

## 🛠️ Files and Directories

- **`api_caller.py`**: Contains functions to make API calls.
- **[bot_builder.py](http://_vscodecontentref_/11)**: Functions to gather website information and build the bot configuration.
- **[conversation.py](http://_vscodecontentref_/12)**: Main script to build or interact with the bot.
- **[customer_service_bot.py](http://_vscodecontentref_/13)**: Core logic for responding to user queries.
- **`repository_handler.py`**: Functions to handle code repository queries.
- **`customer_service_bot_config.json`**: Configuration file for the bot.
- **`requirements.txt`**: List of dependencies.

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](http://_vscodecontentref_/14) file for details.

## 📧 Contact

For any questions or suggestions, please contact [support@split-money-app.com](mailto:support@split-money-app.com).

---

Made with ❤️ by [Your Name](https://github.com/yourusername)
