import json
import pandas as pd
from typing import Optional
from fastapi import FastAPI

app = FastAPI()

#return the ipl match data
@app.get("/match")
async def match_data(team:Optional[str] = None,city:Optional[str] = None,winner:Optional[str] = None):
    df = pd.read_csv("data/IPL Matches 2008-2020.csv")
    json_data = df.to_json(orient="records")
    if team:
        rows_with_team = df[(df['team1'] == team) | (df['team2'] == team)]
        json_data = rows_with_team.to_json(orient="records")
    if city:
        rows_with_city = df[df['city'] == city]
        json_data = rows_with_city.to_json(orient="records")
    if winner:
        rows_with_winner = df[df['winner'] == winner]
        json_data = rows_with_winner.to_json(orient="records")
    data = json.loads(json_data) 
    return data
