#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import requests


def number_of_subscribers(subreddit):

    url = f"https://api.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "your_unique_user_agent"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()

        data = response.json()
        if data['kind'] != 't5':
            raise ValueError("Invalid subreddit or incorrect endpoint")

        return data['data']['subscribers']

    except (requests.exceptions.RequestException, ValueError) as e:
        print(f"Error retrieving subscriber count: {e}")
        return 0


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit = sys.argv[1]
        subscribers = number_of_subscribers(subreddit)
        print(f"Number of subscribers for r/{subreddit}: {subscribers}")
