# IPLAPI - Indian Premier League API

The IPLAPI is a RESTful API that provides access to match statistics and player stats for the Indian Premier League (IPL) cricket tournament. This API is built using FastAPI, ensuring fast and efficient data retrieval. You can access the API's endpoints to retrieve match statistics from 2008 to 2020 and player statistics.

## Endpoints

### Get Match Statistics

Retrieve match statistics for the Indian Premier League from the years 2008 to 2020.

```
Endpoint: /matches
Method: GET
Response Format: JSON
```
Example Request

```
GET /matches
```
Example Response

```
[
    {
        "id": 335982,
        "city": "Bangalore",
        "date": "2008-04-18",
        "player_of_match": "BB McCullum",
        "venue": "M Chinnaswamy Stadium",
        "neutral_venue": 0,
        "team1": "Royal Challengers Bangalore",
        "team2": "Kolkata Knight Riders",
        "toss_winner": "Royal Challengers Bangalore",
        "toss_decision": "field",
        "winner": "Kolkata Knight Riders",
        "result": "runs",
        "result_margin": 140.0,
        "eliminator": "N",
        "method": null,
        "umpire1": "Asad Rauf",
        "umpire2": "RE Koertzen"
    },
    ...
]
```

### Get Player Statistics

Retrieve player statistics for the Indian Premier League.

```
Endpoint: /players
Method: GET
Response Format: JSON
```
Example Request

```
GET /players
```

Example Response

```
[
    {
        "Unnamed: 0": 0,
        "player": "A Ashish Reddy",
        "runs": 280,
        "boundaries": 31,
        "balls_faced": 196,
        "wickets": 18.0,
        "balls_bowled": 270.0,
        "runs_conceded": 400.0,
        "matches": 28,
        "batting_avg": 10.0,
        "batting_strike_rate": 142.86,
        "boundaries_percent": 15.82,
        "bowling_economy": 8.89,
        "bowling_avg": 22.22,
        "bowling_strike_rate": 15.0,
        "catches": 8.0,
        "stumpings": 0.0
    },
    ...
]
```
## Setup 
To setup project locally first clone the repo and run `bash setup.sh`

## How to Use

To access the IPLAPI and retrieve match and player statistics, you can make GET requests to the respective endpoints mentioned above. The responses will be in JSON format, containing the relevant data fields.

## Host Link

You can access the IPLAPI on [RapidAPI](https://rapidapi.com/arunavabasudev-YBvVIHCgEmE/api/ipl-api1), which provides an easy way to explore and use the API's endpoints.

## Deployment

The IPLAPI is deployed using Railway, which offers seamless hosting and deployment solutions. This ensures that the API endpoints are always available and responsive.

## Contributing

Contributions to the IPLAPI project are welcome! If you have any suggestions, improvements, or feature requests, please feel free to open an issue or submit a pull request on the GitHub repository.

## License

This project is licensed under the MIT License, which means you're free to use, modify, and distribute the code as long as you include the appropriate attribution and adhere to the license terms.
