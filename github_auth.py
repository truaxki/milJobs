"""Module for handling GitHub authentication and API access."""

import os
import requests
from dotenv import load_dotenv

def check_github_auth():
    # Force reload of environment variables
    load_dotenv(override=True)

    # Get the token and check its format
    token = os.environ.get("GITHUB_PERSONAL_ACCESS_TOKEN")

    # Debug information (secure version)
    print("=== Debug Information ===")
    if os.path.exists('.env'):
        print("✅ .env file found")
        print(f"Token status: {'Present' if token else 'Missing'}")
        if token:
            print(f"Token length: {len(token)}")
            print(f"Token format: {token[:4]}...{token[-4:]}")  # Only shows first/last 4 chars
    else:
        print("❌ .env file not found!")

    if token:
        headers = {
            'Authorization': f'token {token}',
            'Accept': 'application/vnd.github+json',
            'X-GitHub-Api-Version': '2022-11-28'
        }
        
        response = requests.get('https://api.github.com/user', headers=headers)
        print(f"\nAPI Response Status: {response.status_code}")
        if response.status_code == 200:
            user_data = response.json()
            print(f"✅ Successfully authenticated as: {user_data.get('login')}")
            return True
        else:
            print("❌ Authentication failed")
            return False

    return False

if __name__ == "__main__":
    # Print current working directory to help debug
    print("\nCurrent working directory:", os.getcwd())
    print("Files in current directory:", os.listdir())
    check_github_auth()
