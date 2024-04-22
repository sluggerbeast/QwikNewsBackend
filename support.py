
import schedule
import time

import json
import uuid
import datetime

def writeNewsToJsonFile(jsondata,fileName="news.json"):
       
    # Open the file in write mode ("w")
    with open(fileName, "w") as outfile:
        # Write the JSON data to the file using json.dump()
        json.dump(jsondata, outfile, indent=4)  
        # Add indentation for readability (optional)

# print("JSON data saved to news.json")

# schedule.every(10).seconds.do(writeNewsToJsonFile)

# while True:
#     schedule.run_pending()
#     time.sleep(1)
