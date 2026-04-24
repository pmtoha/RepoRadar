import os
import requests

class GitHubClient:
    def __init__(self):
        self.token = os.getenv("GITHUB_TOKEN")
        self.base_url = "https://api.github.com"
        self.headers = {}
        if self.token:
            self.headers["Authorization"] = f"token {self.token}"

    def search_repos(self, query):
        url = f"{self.base_url}/search/repositories"
        params = {"q": query, "sort": "stars", "per_page": 5}
        response = requests.get(url, headers=self.headers, params=params)
        
        if response.status_code == 200:
            return response.json().get('items', [])
        return []

    def get_repo_details(self, full_name):
        url = f"{self.base_url}/repos/{full_name}"
        response = requests.get(url, headers=self.headers)
        
        if response.status_code == 200:
            return response.json()
        return None