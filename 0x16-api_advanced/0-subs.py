import requests


def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'MyRedditClient'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        if 'subscribers' in data['data']:
            return data['data']['subscribers']
        else:
            return 0
    else:
        return 0


if __name__ == "__main__":
    subreddit = input("Enter a subreddit: ")
    subscribers = number_of_subscribers(subreddit)
    if subscribers == 0:
        print("nonexisting subreddit")
    else:
        print("existing Subreddit")
