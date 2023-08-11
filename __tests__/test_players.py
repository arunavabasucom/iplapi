####Adds higher directory to python modules path.####
import sys
sys.path.append("..") 
####Adds higher directory to python modules path.####
import json
import pandas as pd
from src.main import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_players_data():
    # load csv and convert and load the json    
    test_data = pd.read_csv('src/data/IPL Player Stat.csv')
    test_json_data = test_data.to_json(orient="records")
    test_data_list = json.loads(test_json_data)
    # get the /match endpoint and get the json 
    response = client.get("/players")    
    response_data = response.json()
    assert response.status_code == 200
    assert response_data == test_data_list
