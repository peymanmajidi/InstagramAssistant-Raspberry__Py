# PyInsta
a simple api for instagram

```python
        r = requests.get(f"https://www.instagram.com/{username}/?__a=1").json()
        followers = r['graphql']['user']['edge_followed_by']['count']
        following = r['graphql']['user']['edge_follow']['count']
        posts = r['graphql']['user']['edge_owner_to_timeline_media']['count']
        return followers, following, posts
```

![shot](screenshot.png)
