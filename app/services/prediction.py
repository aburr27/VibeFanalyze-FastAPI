# Simple prediction logic

def predict_winner(home_score_avg: float, away_score_avg: float):
    """
    Basic prediction logic
    """
    if home_score_avg > away_score_avg:
        return "Home Team Likely Wins"
    elif away_score_avg > home_score_avg:
        return "Away Team Likely Wins"
    else:
        return "Even Match"