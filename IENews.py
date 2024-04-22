import requests
from bs4 import BeautifulSoup
import uuid
import time
import json

category = "category"
keywords = "keywords"
IEurl= "https://indianexpress.com/section/"

categoryList = [
  { id: 1, category: "political-pulse", keywords: ["politics", "bjp", "congress", "voting", "election",
"cities","national","political-pulse","india"] },

  { id: 2, category: "sports", keywords: ["sports", "ipl", "footbal",] },
  { id: 3, category: "health", keywords: ["health", "lifestyle",] },
  { id: 4, category: "technology/science", keywords: ["technology",] },
  { id: 5, category: "entertainment", keywords: ["entertainment", "celebrity", "actor", "movies"] },
  { id: 6, category: "business", keywords: ["business", "investment", "funding"] },
  { id: 7, category: "", keywords: ["miscellaneous","explained",] },
  { id: 8, category: "education", keywords: ["education", "college", "school"] },
  { id: 9, category: "startup", keywords: ["startup", "investor"] },
  
  { id: 10, category: "lifestyle", keywords: ["travel"] },
  { id: 11, category: "", keywords: ["science"] },
  { id: 12, category: "fashion", keywords: ["fashion", "outfit"] },
  { id: 13, category: "international", keywords: ["international", "world"] },

]

def writeNewsToJsonFile(jsonfile):
       
    # Open the file in write mode ("w")
    with open("news.json", "w") as outfile:
        # Write the JSON data to the file using json.dump()
        json.dump(jsonfile, outfile, indent=4)  
        # Add indentation for readability (optional)
def extractCat(url):
    url_parts = url.split("/")

    # Extract the desired element (assuming "education" is the third element)
    category = url_parts[4]
    return category

def parse_html_for_news(html_content):
    """
    Parses HTML content to extract shorts information (for educational purposes only).

    Args:
        html_content (str): The HTML content to be parsed.

    Returns:
        list: A list of dictionaries containing extracted information (if successful).
              Empty list if parsing fails.
    """

    soup = BeautifulSoup(html_content, 'html.parser')

    # Adjust selectors based on website structure (replace placeholders)
    articles = soup.find_all('div', class_='articles')  # Assuming articles are within 'shorts-card' elements
    
    # print(articles)

    scraped_data = []
    for article in articles:
        
        date = article.find('div',class_='date').text.strip()
        # print(date)
        img_url = article.find('img').get("src")
        title_element = article.find('h2', class_='title').find('a')
        title_text = ""
        page_url = ""
        # if(title_element!=None):
        #     print("inside none")
        title_text = title_element.get('title')
        page_url = title_element.get('href')
        # else:
        #     title_element = article.find('div', class_='title')
        #     title_text = title_element.find('a').get('title')
        #     page_url = title_element.get('href')
        # print(page_url)
        # print(title_text)
           
        image_element = article.find('img')
        image_url = image_element.get('src')
        content_element = article.find("p")
        if(content_element!=None):
           content = content_element.text.strip()
        else:
            content = title_text
        

        if title_element and content_element:
            scraped_data.append({
                'id': uuid.uuid4().hex,
                'title': title_element.text.strip(),
                'description': content,
                'urlToImage': img_url,
                "url": page_url,
                "category": extractCat(page_url),
                "date":date.split(",")[0],
            })

    #         # "articles": [
    # {
    #   "source": { "id": null, "name": "News18" },
    #   "author": "S Aadeetya",
    #   "title": "Worrying Boat Data Breach: More Than 7.5 Million Customers At Risk Of Major Cyber Attack - News18",
    #   "description": "Boat sells its affordable audio and wearable products in the Indian market and its buyers will be worried about the latest news of a data breach.",
    #   "url": "https://www.news18.com/tech/major-boat-data-breach-more-than-7-5-million-customers-at-risk-of-major-cyber-attack-8843640.html",
    #   "urlToImage": "https://images.news18.com/ibnlive/uploads/2023/11/deepfake-2023-11-72778687d939b3f2f757301ea32e4824-16x9.jpg?impolicy=website&width=1200&height=675",
    #   "publishedAt": "2024-04-08T16:45:55Z",
    #   "content": "Boat from India has reportedly faced a major breach that affects more than 7 million customers of the audio company. Boat is one of the top selling brands in the affordable audio segment, which has c… [+1992 chars]"
    # }
    
    return scraped_data


def fetch_html_source(IEurl):
  """
  Fetches the HTML source of a web page using its URL.

  Args:
      url (str): The URL of the web page.

  Returns:
      str: The HTML source of the web page, or None if an error occurs.
  """
  try:
    response = requests.get(IEurl)
    response.raise_for_status()  # Raise an error for failed requests
    return response.text
      # Access the HTML content as text
  except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
    return None
def IE_News(url,category):
#    print(url+category)
   val = fetch_html_source(url+category)
   return parse_html_for_news(val)

def extractCat(url):
    if(not url):
       return ""
    url_parts = url.split("/")

    # Extract the desired element (assuming "education" is the third element)
    category = url_parts[4]
    return category
   
   
# print(IE_News(IEurl,"entertainment"))
def get_news():
   
    cat = [
   "political-pulse",
   "sports",
   "business",
   "technology",
    "education"]
    
    news_array = []
    for i in cat:
    #    print(i)
       news_array.extend(IE_News(IEurl,i))
    # news_data = {category: IE_News(IEurl,category) for category in cat}
    writeNewsToJsonFile({"data": {
    "category_list":cat,
    "news_list": news_array 
    }})
    print(len(news_array))

# Print the JSON data
# get_news()
# print(len(news_array))
