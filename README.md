# iplapi

- endpoints
```
v0.1(https://ipl-api1.p.rapidapi.com/)

/playes-> to list all of the players
/match-> to list all of the matches
/match?team=Kolkata Knight Riders-> to get matches for a particular team
/match?city=Kolkata-> to get matches by city
/match?winner=Kolkata Knight Riders->to get by winner
```

```bash
curl --request GET \
	--url https://ipl-api1.p.rapidapi.com/match \
	--header 'x-rapidapi-host: ipl-api1.p.rapidapi.com' \
	--header 'x-rapidapi-key: API_KEY'
```


- setup

```bash
# clone repo
git clone git@github.com:arunavabasucom/iplapi.git
# install python packages
pip install -r requirements.txt
# start the server
uvicorn src.main:app --reload
```


