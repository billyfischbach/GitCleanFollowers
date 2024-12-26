import requests

# Replace 'your_token_here' with your personal access token
TOKEN = 'XXXXX'
USERNAME = 'GitHubUsername'

def get_following():
    url = f'https://api.github.com/users/{USERNAME}/following'
    headers = {'Authorization': f'token {TOKEN}'}
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"Failed to fetch following list: {response.status_code}")
        return []
    return [user['login'] for user in response.json()]

def get_followers():
    url = f'https://api.github.com/users/{USERNAME}/followers'
    headers = {'Authorization': f'token {TOKEN}'}
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"Failed to fetch followers list: {response.status_code}")
        return []
    return [user['login'] for user in response.json()]

def unfollow_user(user):
    url = f'https://api.github.com/user/following/{user}'
    headers = {'Authorization': f'token {TOKEN}'}
    response = requests.delete(url, headers=headers)
    if response.status_code == 204:
        print(f'Successfully unfollowed {user}')
    else:
        print(f'Failed to unfollow {user}: {response.status_code}')

def main():
    following = set(get_following())
    followers = set(get_followers())

    non_followers = following - followers

    for user in non_followers:
        unfollow_user(user)

if __name__ == '__main__':
    main()