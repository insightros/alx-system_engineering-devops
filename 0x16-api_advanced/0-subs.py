import requests


def number_of_subscribers(subreddit):
    headers = {"User-Agent": "MyRedditClient/1.0"}
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get("data", {})
        return data.get("subscribers", 0)
    else:
        return 0
