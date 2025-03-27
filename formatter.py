import json

with open("data/leagues.json") as f:
    LEAGUES = json.load(f)

with open("data/teams.json") as f:
    TEAMS = json.load(f)

def format_fixture(match):
    league = LEAGUES.get(match["league"], "🔰")
    home_team = TEAMS.get(match["home"], {}).get("home", "⚪")
    away_team = TEAMS.get(match["away"], {}).get("away", "⚫")

    return f"""
📌 𝗧𝗼𝗱𝗮𝘆'𝘀 𝗠𝗮𝘁𝗰𝗵𝗲𝘀  

{league} {match['league']} | {match['stage']}  
{home_team} {match['home']} 🆚 {match['away']} {away_team}  
🕡 {match['local_time']} Local | {match['utc_time']} UTC 🌐
    """

def format_result(match):
    return f"""
📌 Match ended  

{match['league_emoji']} {match['league']} | {match['stage']}  
{match['home']} {match['home_score']}️⃣-{match['away_score']}️⃣ {match['away']}  
{match['scorers']}
🎖️ Man of the Match: {match['motm']}
    """

def format_postponed(match):
    return f"""
Match postponed ❗  

{match['league']} | {match['stage']}  
{match['home']} 🆚 {match['away']}  
Reason: {match['reason']}
    """
