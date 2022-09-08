import json
import uvicorn
from fastapi import FastAPI
import urllib.request

url = "https://raw.githubusercontent.com/oit-tools/syllabus-scraping/master/data/2022.json"
session = urllib.request.urlopen(url)
data = json.loads(session.read())

app = FastAPI()

@app.get("/{numbering}")
async def get_syllabus(numbering: str):
    return data[numbering]

def main():
    uvicorn.run(app, host="localhost", port=8000, reload=True)


if __name__ == "__main__":
    main()
