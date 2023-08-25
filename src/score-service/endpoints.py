
def get_scores(size: int = None, level: int = None):
    return [
        {'name': 'player1', 'score': 14000, 'level': 0},
        {'name': 'player2', 'score': 4000, 'level': 1},
        {'name': 'player3', 'score': 84000, 'level': 0}
    ]


def save_score(score: int, level: int, name: str):
    return {
        'position': 30
    }
