import json
import uvicorn
from fastapi import FastAPI
import requests

url = "https://raw.githubusercontent.com/a-kaibu/syllabus-scraping/master/2022.json?token=GHSAT0AAAAAABT4CTWQN5O46JGYAPCV6XBUYYKADNQ"
session = requests.Session()
data = session.get(url)
json_data = json.loads(data.text)

app = FastAPI()

@app.get("/{numbering}")
async def get_syllabus(numbering: str):
    return json_data[numbering]

def main():
    uvicorn.run(app, host="localhost", port=8000, reload=True)


if __name__ == "__main__":
    main()
