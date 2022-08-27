import json
import uvicorn
from fastapi import FastAPI


with open("./2022.json") as f:
    data = json.load(f)

app = FastAPI()

@app.get("/{numbering}")
async def get_syllabus(numbering: str):
    return data[numbering]

def main():
    uvicorn.run(app, host="localhost", port=8000, reload=True)


if __name__ == "__main__":
    main()
