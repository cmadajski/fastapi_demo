from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import json

# create new FastAPI instance named "app"
app = FastAPI()

about = {
    "owner": "Christian Madajski",
    "linkedin": "https://www.linkedin.com/in/cmadajsk/",
    "github": "https://github.com/cmadajski"
}

urls = {
    "arstechnica": "https://www.arstechnica.com",
    "google": "https://www.google.com",
    "facebook": "https://www.meta.com",
    "github": "https://github.com"
}

class Website(BaseModel):
    name: str
    url: str
    category: str

class UpdateWebsite(BaseModel):
    # whenever using None as a default value, it's good practice to use Optional for type hinting
    # this means that name must either have string type or None type, others will throw errors
    # this is important for when a put method changes less than all data values
    name: Optional[str] = None
    url: Optional[str] = None
    category: Optional[str] = None

# basic GET endpoint for "app"
@app.get("/")
def index():
    return {"name": "first data"}

@app.get("/get_urls")
def get_urls():
    return json.dumps(urls)

# path parameters are similar to f-strings, it is required to have brackets in the path
@app.get("/get_url/{name}")
def get_url_path(name: str):
    try:
        return urls[name]
    except KeyError:
        return f"KeyError: There is no url for {name} in the system."

# query parameters are automatically processed, just define them as parameters
@app.get("/get_url")
def get_url_query(name: str):
    return None

@app.post("/create_website/{name}")
def create_website(name: str, website: Website):
    if name in urls:
        return {"Error": "URL already exists"}
    else:
        urls

# put method requires special considerations


#@app.put("/update_website")
# to run app using uvicorn, use command "uvicorn myapi:app --reload"