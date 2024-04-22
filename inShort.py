# Coded by Sumanjay on 29th Feb 2020
import datetime
import uuid
import requests



headers = {
    'authority': 'inshorts.com',
    'accept': '*/*',
    'accept-language': 'en-GB,en;q=0.5',
    'content-type': 'application/json',
    'referer': 'https://inshorts.com/en/read',
    'sec-ch-ua': '"Not/A)Brand";v="99", "Brave";v="115", "Chromium";v="115"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'sec-gpc': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
}

params = (
    ('category', 'top_stories'),
    ('max_limit', '100'),
    ('include_card_data', 'true')
)


def getNews(category,count=50):
    if category == 'all':
        print("inside all")
        response = requests.get(
            f'https://inshorts.com/api/en/news?category=all_news&max_limit={count}&include_card_data=true')
    else:
        response = requests.get(
            f'https://inshorts.com/api/en/search/trending_topics/{category}', headers=headers, params=params)
    try:
        news_data = response.json()['data']['news_list']
        print("No errors in news_data")
    except Exception as e:
        # print(response.text)
        news_data = None

    newsDictionary = {
        'success': True,
        'category': category,
        'data': []
    }

    if not news_data:
        print("inside news_data error")
        newsDictionary['success'] = response.json()['error']
        newsDictionary['error'] = 'Invalid Category'
        return newsDictionary
    print(len(news_data)) 
    for entry in news_data:
        try:
            news = entry['news_obj']
            author = news['author_name']
            title = news['title']
            imageUrl = news['image_url']
            url = news['shortened_url']
            content = news['content']
            category= news['category_names']

            timestamp = int(news['created_at'])
           
            readMoreUrl = news['source_url']

            newsObject = {
                'id': uuid.uuid4().hex,
                'title': title,
                'imageUrl': imageUrl,
                'url': readMoreUrl,
                'content': content,
                'author': author,
                'date': unixToUtc(timestamp),
                "categoryList":category,
                'readMoreUrl': readMoreUrl
            }
            newsDictionary['data'].append(newsObject)
            # print(newsObject)
        except Exception:
            print("some went wrong inside exception")
            
    # print(newsDictionary['data'])
    return newsDictionary['data']

def unixToUtc(time):


    timestamp = int(time/1000)
    # print(timestamp)
    date_time_obj = datetime.datetime.fromtimestamp(timestamp)
    
    # You can format the date time object as needed
    formatted_date_time = date_time_obj.strftime("%d-%m-%Y %H:%M:%S")
    # print(formatted_date_time)
    return formatted_date_time
# unixToUtc(1712916790000)
# print(getNews("politics"))