RepoRadar 🦅
RepoRadar is a smart Telegram bot designed for developers to discover, analyze, and save interesting GitHub repositories without leaving the chat.

🗂️ Project Roadmap & Structure
This project follows a modular architecture. The structure separates the bot logic, API interactions, and data handling for better scalability.

Directory Tree
RepoRadar/├── .env.example           # Example of how to set up tokens├── .gitignore             # Ignore venv and .env files├── requirements.txt       # List of dependencies├── README.md              # Setup instructions and screenshots├── main.py                # Entry point of the application├── bot/│   ├── __init__.py│   ├── handlers.py        # Command handlers (/start, /search)│   ├── keyboards.py       # Inline buttons and layouts│   └── messages.py        # Text formatting strings├── github/│   ├── __init__.py│   └── client.py          # Logic to call GitHub API└── database/    ├── __init__.py    └── db_manager.py      # SQLite connection and queries
🚀 Quick Setup (Automated)
To save time, you can copy and run the following bash command in your terminal. This will create all the necessary directories and files instantly.

bash

# Create the main project folder and navigate into it
mkdir RepoRadar && cd RepoRadar

# Create the subdirectories
mkdir bot github database

# Create all required files
touch .env .gitignore requirements.txt README.md main.py
touch bot/__init__.py bot/handlers.py bot/keyboards.py bot/messages.py
touch github/__init__.py github/client.py
touch database/__init__.py database/db_manager.py

echo "✅ Project structure created successfully!"
⚙️ Installation
1. Prerequisites
Ensure you have Python 3.9+ installed on your machine.

2. Install Dependencies
Navigate to the RepoRadar folder and install the required libraries:

bash

pip install -r requirements.txt
3. Environment Configuration
Create a .env file in the root directory (or rename .env.example) and add your tokens:

env

BOT_TOKEN=your_telegram_bot_token_here
GITHUB_TOKEN=your_github_personal_access_token_here
Where to get tokens:

BOT_TOKEN: Talk to @BotFather on Telegram and create a new bot.
GITHUB_TOKEN: Go to GitHub Settings > Developer Settings > Personal Access Tokens. (Optional but recommended for higher API rate limits).
📱 Bot Commands
Command
Description
/start	Initialize the bot and view welcome message.
/search <query>	Search for repositories (e.g., /search python).
/mylist	View your personally saved list of repositories.

▶️ Running the Bot
Once your environment is configured, simply run the entry point script:

bash

python main.py
You should see a console output indicating the bot is running. Open your Telegram bot and start searching!

🛠️ Tech Stack
Language: Python 3.9+
Framework: python-telegram-bot (v20+)
API: GitHub REST API
Database: SQLite3
📄 License
This project is open source and available under the MIT License.