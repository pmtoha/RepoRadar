from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def build_search_results_keyboard(repos):
    keyboard = []
    for repo in repos:
        full_name = repo['full_name']
        stars = repo['stargazers_count']
        # Button data: 'details_owner/repoName'
        button = InlineKeyboardButton(f"{full_name} ({stars}⭐)", callback_data=f"details_{full_name}")
        keyboard.append([button])
    return InlineKeyboardMarkup(keyboard)

def build_details_keyboard(full_name):
    keyboard = [
        [
            InlineKeyboardButton("Save to List ⭐", callback_data=f"save_{full_name}"),
            InlineKeyboardButton("Open on GitHub 🔗", url=f"https://github.com/{full_name}")
        ]
    ]
    return InlineKeyboardMarkup(keyboard)