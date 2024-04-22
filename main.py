# main.py

from fastapi import FastAPI, Request
from pydantic import BaseModel
import json
import short
import inShort
import IENews
# import support
# from fastapi_utils.tasks import repeat_every

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
def writeToJsonFile(jsondata,fileName="news.json"):
       
    # Open the file in write mode ("w")
    with open(fileName, "w") as outfile:
        # Write the JSON data to the file using json.dump()
        json.dump(jsondata, outfile, indent=4)  
        # Add indentation for readability (optional)


from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# @repeat_every(seconds=2)  # 1 hour
# async def doItS():
#      writeNewsToJsonFile()

#Current working method But plans to update.


#I want to make it a main function to fectch news.
def res():
    try:
      return load_news_data("news.json")
    finally:
      print("started fetching news")
      IENews.get_news()
   
   

@app.get("/")
async def root():
    return short.fetch_html_sourceIE()
    

@app.get("/news")
async def root():
    
    return res() 
#This function is loading news data from news.json and sending as response.
#File news.json is updated with latest news in a different func.

@app.get("/inshorts")
async def shorts(count:int=50,category:str="all"):
    print("get for inshorts")
    return inShort.getNews(category,count)

@app.get("/showvisits")
async def showvisits():
    # print("get for inshorts")
    val = load_news_data("visits.json")
    # print(val)
    return val 


class Visits(BaseModel):
   ip:str | None = None
   date:str
   time:str
   location:str | None = None
   event:str | None = None
   app:str

@app.post("/visits")
async def visits(visits:Visits,request:Request):
  
  val = load_news_data("visits.json") 
  visits.ip = request.client.host 
  val.insert(0,visits.dict())
  writeToJsonFile(val,"visits.json")
  return "200"
