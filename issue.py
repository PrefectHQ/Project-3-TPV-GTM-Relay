import requests

def issue_comment(owner:str, repo:str, issue_number:str, message:str, token:str):
    """Issue comment event."""
    token = f"Authorization: Bearer {token}"
    requests.post(f"/repos/{owner}/{repo}/issues/{issue_number}/comments",body=message, headers=token)