import pandas as pd
from fastapi import APIRouter
import json

router = APIRouter()

@router.get("/players")
async def players_data():
    # loading the csv as a dataframe
    df = pd.read_csv("src/data/IPL Player Stat.csv")
    # converting json
    json_data = df.to_json(orient="records")
    data = json.loads(json_data)
    return data
