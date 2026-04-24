def get_repo_card(repo):
    """Formats a single repository details card."""
    name = repo.get('name', 'N/A')
    owner = repo.get('owner', {}).get('login', 'N/A')
    stars = repo.get('stargazers_count', 0)
    forks = repo.get('forks_count', 0)
    lang = repo.get('language', 'Unknown')
    desc = repo.get('description', 'No description provided.')
    url = repo.get('html_url', '#')

    return (
        f"⭐ <b>{name}</b> by {owner}\n"
        f"🔹 Language: {lang}\n"
        f"🔹 Stars: {stars} | Forks: {forks}\n\n"
        f"📝 {desc}\n"
        f"🔗 {url}"
    )

def get_saved_list(repos):
    if not repos:
        return "You haven't saved any repositories yet."
    
    msg = "📂 <b>Your Saved Repositories:</b>\n\n"
    for name, url in repos:
        msg += f"• <a href='{url}'>{name}</a>\n"
    return msg