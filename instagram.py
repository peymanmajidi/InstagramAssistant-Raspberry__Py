import requests

def fetch_data(username):
    try:
        r = requests.get(f"https://www.instagram.com/{username}/?__a=1").json()
        followers = r['graphql']['user']['edge_followed_by']['count']
        following = r['graphql']['user']['edge_follow']['count']
        posts = r['graphql']['user']['edge_owner_to_timeline_media']['count']
        return followers, following, posts
    except:
        return -1, -1, -1
