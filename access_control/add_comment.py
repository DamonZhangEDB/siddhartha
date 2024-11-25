import os
from datetime import datetime

import requests

# Retrieve environment variables
issue_number = os.environ.get('ISSUE_NUMBER')
owner_repo = os.environ.get('OWNER_REP')
github_token = os.environ.get('GITHUB_TOKEN')

# Check if environment variables are set
if not issue_number:
    print('ISSUE_NUMBER environment variable not set.')
    exit(1)

if not owner_repo:
    print('OWNER_REP environment variable not set.')
    exit(1)

if not github_token:
    print('GITHUB_TOKEN environment variable not set.')
    exit(1)

# Split owner and repository from OWNER_REP
owner, repo = owner_repo.split('/')

# Construct the API URL
url = f'https://api.github.com/repos/{owner}/{repo}/issues/{issue_number}/comments'

# Set headers for authentication and content type
headers = {
    'Accept': 'application/vnd.github+json',
    'Authorization': f'Bearer {github_token}'
}

current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')


header = "The following users have non-managed escalation policies that should be removed first:"
errors = [
    "user 1(user1@example.com) with [ep1, ep2]",
    "user 2(user2@example.com) with [ep3, ep2]",
    "user 3(user3@example.com) with [ep1, ep3]",
]
error = '\n'.join(errors)

msg = f"@{current_date}\n{header}\n{error}"

# Define the comment body
data = {
    'body': msg
}

# Make the POST request to add the comment
try:
    response = requests.post(url, headers=headers, json=data)
    response.raise_for_status()
    print('Comment added successfully.')
except requests.exceptions.HTTPError as errh:
    print('HTTP Error:', errh)
    print('Response content:', response.content)
except requests.exceptions.ConnectionError as errc:
    print('Error Connecting:', errc)
except requests.exceptions.Timeout as errt:
    print('Timeout Error:', errt)
except requests.exceptions.RequestException as err:
    print('Error:', err)
