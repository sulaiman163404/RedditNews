import requests
import json


def format_date(timestamp_obj):
    from datetime import datetime
    datetime_obj = datetime.fromtimestamp(timestamp_obj)
    return str(datetime_obj)


def get_data(url):
    response = requests.get(url, headers={'user-agent': 'your bot 0.1'})
    # print(response.text)
    # print(type(response.text))
    python_obj = json.loads(response.text)
    news = python_obj['data']['children']
    # print(news)
    filtered_data = []
    
    number = 1
    for new in news:
        news_data = {
            f'News number {number}': {
                'title': new['data']['title'],
                'author': new['data']['author'],
                'created': format_date(new['data']['created'])
            }

        }
        filtered_data.append(news_data)
        number += 1

    return filtered_data

def write_to_json(data):
    with open('RedditNews.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)

def main(url):
    data = get_data(url)
    # print(data)
    write_to_json(data)


main('https://www.reddit.com/r/science/.json')

'olala'