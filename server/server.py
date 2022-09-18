from typing import Union
import requests
from fastapi import FastAPI, Request,Body
import json
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os

app = FastAPI()

class Item():
    def __init__(self):
        self.item = {
            "asyncId": "55f251ed70",
            "options": {
                "carSpace": "exclusive",
                "cars": [
                    {
                        "building": 1,
                        "group": 1,
                        "car": 3
                    }
                ],
                "destination": {
                    "destinationFloor": 0,
                    "destinationZone": "Floor 0"
                }
            },
            "target": {
                "floor": 3
            }
        }

@app.get("/")
def read_root():
    return {"hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int , q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/test/{item_id}")
def read_item(item_id: str ):
    aitem_id = item_id.replace("\'", "\"")
    print(json.loads(item_id))
    requests.post("https://hack.myport.guide/publish/", json=json.loads(item_id))
    return

@app.post("/floor/}")
async def get_body(body: str = Body(..., media_type='text/plain')):
    requests.post("https://hack.myport.guide/publish/", json=body.json())
    return await body

"""
@app.get('/favicon.ico')
async def favicon():
    file_name = "favicon.ico"a
    file_path = os.path.join(app.root_path, "static")
    return FileResponse(path=file_path, headers={"Content-Disposition": "attachment; filename=" + file_name})
"""