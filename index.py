import datetime
import requests
import json

now = datetime.datetime.now()

if (now.month < 3):
    year = now.year - 1
else:
    year = now.year

league_id = 1204492

scores = {}
for week in range(1, 8):
    r = requests.get(
        'http://games.espn.com/ffl/api/v2/scoreboard', 
        params={
            'leagueId': league_id, 
            'seasonId': year, 
            'matchupPeriodId': week
        })
    scores[week] = r.json()

# data = json.loads(scores.metadata)

print(scores)
