# main.py

from fastapi import FastAPI
import json
import short
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
    # for news_item in articles:
    #     print(f"Title: {news_item['title']}")
    #     print(f"Content: {news_item['description']}")
    #     print("-" * 20)
    else:
        print("Error: Could not load news data.")
    # return articles
    return short.fetch_html_source()

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return News()