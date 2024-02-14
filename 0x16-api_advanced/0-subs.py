import requests


def number_of_subscribers(subreddit):
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'User-Agent': 'my-reddit-api-client'}
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        if data['kind'] == 't5':
            return data['data']['subscribers']
        else:
            return 0
    except requests.exceptions.HTTPError as err:
        if response.status_code == 404:
            return 0
        else:
            raise err
