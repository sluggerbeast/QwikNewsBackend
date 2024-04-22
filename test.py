

from newsapi import NewsApiClient

# key = "578ee64b2fe8401a98ecea5c88e1048f"
# newsapi = NewsApiClient(api_key=key)
# all_articles = newsapi.get_everything(q='india')

# print(all_articles['articles'][0]['source']) 
#print(type(all_articles['articles'][0]['source'])) 

import json

def load_news_data(filename):
  """
  Loads news data from a JSON file.

  Args:
      filename (str): The path to the JSON file containing news data.

  Returns:
      dict: A dictionary containing the loaded news data, 
            or None if an error occurs.
  """
  try:
    # Open the JSON file in read mode
    with open(filename, 'r') as file:
      # Load the JSON data into a dictionary
      data = json.load(file)
      print(type(data))
    return data
  except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")
    return None
  except json.JSONDecodeError as e:
    print(f"Error: Failed to parse JSON data. {e}")
    return None

def News():

  
# Example usage
    filename = 'news.json'
    news_data = load_news_data(filename)

    if news_data:
  # Access data using dictionary keys
  # (Replace 'title' and 'content' with actual keys from your JSON data)
  # print(news_data['articles'][0]['title'])
        articles = news_data['articles']
    for news_item in articles:
        print(f"Title: {news_item['title']}")
        print(f"Content: {news_item['description']}")
        print("-" * 20)
    else:
        print("Error: Could not load news data.")

# News()
url = "https://indianexpress.com/shorts/education/2-difficulty-levels-for-additional-language-in-cbse-class-12-under-govt-consideration-9266992/"

# Split the URL by '/' (forward slash)
url_parts = url.split("/")

# Extract the desired element (assuming "education" is the third element)
education_section = url_parts[4]

print(education_section)
print(url_parts)
