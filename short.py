import requests
from bs4 import BeautifulSoup
import time  # For introducing delays between requests

def parse_html_for_shorts(html_content):
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
    articles = soup.find_all('div', class_='swiper-slide')  # Assuming articles are within 'shorts-card' elements
    
    # print(articles)

    scraped_data = []
    for article in articles:
        title_element = article.find('h2', class_='shorts_top_heading')  # Assuming title is within an h3 with class 'title'
        content_element = article.find('p', class_='shorts_artcle_summery')  # Assuming content is within a p with class 'description'
        short_img_url = article.find('img')
        image_url = short_img_url.get('src')
        page_url = article.find("a",id="ie_shorts_readfull_h").get('href')
        # print(page_url)
          # Check if the 'src' attribute exists
            
        # print(image_url)
        # print(title_element)
        if title_element and content_element:
            scraped_data.append({
                'title': title_element.text.strip(),
                'description': content_element.text.strip(),
                'urlToImage': image_url,
                "url": page_url
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

def fetch_html_source(url= "https://indianexpress.com/shorts/"):
  """
  Fetches the HTML source of a web page using its URL.

  Args:
      url (str): The URL of the web page.

  Returns:
      str: The HTML source of the web page, or None if an error occurs.
  """
  try:
    response = requests.get(url)
    response.raise_for_status()  # Raise an error for failed requests
    return parse_html_for_shorts(response.text)
      # Access the HTML content as text
  except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
    return None

# Example usage
url = "https://indianexpress.com/shorts/"

# print(html_content)

data = fetch_html_source()
print(type(data))

# if data:
#     for item in data:
#         print(f"Title: {item['title']}")
#         print(f"Content: {item['description']}")
#         print(f"img:  {item['urlToImage']}")
#         print(f"Page url {item["url"]}\n")
#         print("-" * 40)
# else:
#     print("Parsing failed or no data found.")
