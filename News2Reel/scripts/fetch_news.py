import yaml
import requests
import json
from datetime import datetime

with open("../config/setting.yaml", "r") as f:
    settings = yaml.safe_load(f)

api_key = settings['api_keys']['cryptopanic']
#print(api_key)

def fetch_news():
#    url = f"https://cryptopanic.com/api/v1/posts/?auth_token={api_key}&filter=rising"
    url = f"https://cryptopanic.com/api/v1/posts/?auth_token={api_key}&filter=rising"
    response = requests.get(url)
    print(response.status_code)
    print(response.text)
    if response.status_code == 200:
        news_data = response.json()
        filename = f"../data/raw_news/news_{datetime.now().strftime('%Y-%m-%d_%H-%M')}.json"
        with open(filename, "w") as f:
            json.dump(news_data, f, indent= 2)
        print("Ok!")
    else:
        print("Not OK!")
if __name__ == '__main__':
    fetch_news()
