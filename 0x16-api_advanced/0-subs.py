import requests


def number_of_subscribers(subreddit):
    headers = {"User-Agent": "MyRedditClient/1.0"}
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json().get("data", {})
        if "subscribers" in data:
            return data["subscribers"]
        else:
            return 0
    else:
        return 0
