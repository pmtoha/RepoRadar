import logging
from telegram import Update
from telegram.ext import ContextTypes
from github.client import GitHubClient
from database.db_manager import Database
from bot.messages import get_repo_card, get_saved_list
from bot.keyboards import build_search_results_keyboard, build_details_keyboard

# Initialize services
gh_client = GitHubClient()
db = Database()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Welcome to **RepoRadar**!\n\n"
        "Commands:\n"
        "/search <query> - Find GitHub repos\n"
        "/mylist - View your saved repos"
    )

async def search(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Please provide a search term. Usage: /search python")
        return

    query = " ".join(context.args)
    await update.message.reply_text(f"🔍 Searching for '{query}'...")

    results = gh_client.search_repos(query)
    
    if not results:
        await update.message.reply_text("No repositories found.")
        return

    keyboard = build_search_results_keyboard(results)
    await update.message.reply_text(
        f"Top results for <b>{query}</b>:", 
        reply_markup=keyboard,
        parse_mode='HTML'
    )

async def my_list(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    repos = db.get_repos(user_id)
    text = get_saved_list(repos)
    await update.message.reply_text(text, parse_mode='HTML', disable_web_page_preview=True)

async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer() # Acknowledge the button click

    data = query.data
    user_id = update.effective_user.id

    if data.startswith("details_"):
        full_name = data.replace("details_", "")
        await query.edit_message_text(text=f"Fetching details for {full_name}...")
        
        repo_data = gh_client.get_repo_details(full_name)
        if repo_data:
            text = get_repo_card(repo_data)
            keyboard = build_details_keyboard(full_name)
            await query.edit_message_text(text=text, reply_markup=keyboard, parse_mode='HTML')
        else:
            await query.edit_message_text("❌ Could not fetch repository details.")

    elif data.startswith("save_"):
        full_name = data.replace("save_", "")
        # Note: In a real app, you'd fetch the URL from DB or API again. 
        # For simplicity, we'll construct it or re-fetch.
        repo_data = gh_client.get_repo_details(full_name)
        if repo_data:
            url = repo_data['html_url']
            success = db.save_repo(user_id, full_name, url)
            if success:
                await query.answer("✅ Repository saved!", show_alert=True)
            else:
                await query.answer("⚠️ Repository already in your list.", show_alert=True)
        else:
            await query.answer("❌ Error saving repository.", show_alert=True)