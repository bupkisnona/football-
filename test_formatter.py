from src.formatter import format_fixture, format_result

def test_format_fixture():
    match = {
        "league": "La Liga",
        "stage": "Match Day 10",
        "home": "Barcelona",
        "away": "Real Madrid",
        "local_time": "20:30",
        "utc_time": "18:30"
    }
    assert "📌 𝗧𝗼𝗱𝗮𝘆'𝘀 𝗠𝗮𝘁𝗰𝗵𝗲𝘀" in format_fixture(match)

def test_format_result():
    match = {
        "league": "La Liga",
        "league_emoji": "🇪🇸",
        "stage": "Final",
        "home": "Barcelona",
        "home_score": 2,
        "away": "Real Madrid",
        "away_score": 1,
        "scorers": "50' Messi, 70' Lewandowski",
        "motm": "Messi"
    }
    assert "📌 Match ended" in format_result(match)
