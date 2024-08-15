#!/usr/bin/python3

import requests

def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit.
    
    Args:
        subreddit (str): The name of the subreddit.
        
    Returns:
        int: Number of subscribers or 0 if subreddit is invalid.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        "User-Agent": "Custom User-Agent: 0-subs:v1.0 (by /u/yourusername)"
    }

    try:
        # Send GET request to Reddit API
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()
            return data['data'].get('subscribers', 0)
        else:
            return 0

    except requests.exceptions.RequestException as e:
        # In case of any exception, return 0
        return 0

