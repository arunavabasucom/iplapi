import pandas as pd
from fastapi import APIRouter, Query
from src.helpers.data_filters import apply_filters
import json
router = APIRouter()

@router.get("/match")
async def match_data(
    team: str = Query(None, description="Team name"),
    city: str = Query(None, description="City name"),
    winner: str = Query(None, description="Winner name")
):
    # loading the csv as a dataframe
    df = pd.read_csv("data/IPL Matches 2008-2020.csv")
    # apply filters
    filtered_data = apply_filters(df, team, city, winner)
    # converting json
    json_data = filtered_data.to_json(orient="records")
    data = json.loads(json_data)

    return data
