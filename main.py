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

@app.get("/table/all")
async def get_table():
    result = list()

    for key in data.keys():
        result.append({
            "lecture_title": data[key]["lecture_title"],
            "year": data[key]["year"],
            "credit": data[key]["credit"],
            "term": data[key]["term"],
            "person": data[key]["person"],
            "numbering": data[key]["numbering"],
            "department": data[key]["department"],
            "dow": data[key]["dow"],
            "period": data[key]["period"],
            "url": data[key]["url"]
        })

    return result

def main():
    uvicorn.run(app, host="localhost", port=8000, reload=True)


if __name__ == "__main__":
    main()
