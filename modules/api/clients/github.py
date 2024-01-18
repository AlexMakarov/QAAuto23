import requests


class GitHub:

    def get_user(self, username):
        r = requests.get(f'https://api.github.com/users/{username}')
        body = r.json()

        return body
    

    def search_repo(self, name):
        r = requests.get(
            'https://api.github.com/search/repositories',
            params = {"q": name})
        
        body = r.json()

        return body
    
    def get_emoji(self, name):
        r = requests.get('https://api.github.com/emojis', name)
        body = r.json

        return body
    
    def get_gists(self, gist_id):
        r = requests.get('https://api.github.com/gists/GIST_ID', gist_id)
        body = r.json

        return body


    def get_events(self, accept):
        r = requests.get('https://api.github.com/events', accept)
        body = r.json

        return body