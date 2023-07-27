####Adds higher directory to python modules path.####
import sys
from mock import patch
sys.path.append("..") 
####Adds higher directory to python modules path.####
import pandas as pd
from fastapi.testclient import TestClient
from src.main import app
from mocks.apply_filter import mock_apply_filters

client = TestClient(app)

def test_match_data():
    # Prepare test data and parameters
    test_df = pd.DataFrame({
        'team1': ['team1', 'team2', 'team3'],
        'team2': ['team4', 'team5', 'team6'],
        'city': ['city1', 'city2', 'city3'],
        'winner': ['team1', 'team5', 'team6']
    })
    team = 'team1'
    city = 'city2'
    winner = 'team5'

    # Mock the apply_filters function
    # def mock_apply_filters(df, team, city, winner):
    #     return test_df

    # Patch the apply_filters function with the mock
    with patch('src.helpers.data_filters.apply_filters', mock_apply_filters):
        # Send request to the route
        response = client.get("/match", params={'team': team, 'city': city, 'winner': winner})
        assert response.status_code == 200

        # Check the response data
        expected_data = test_df.to_dict(orient='records')
        assert response.json() == expected_data
