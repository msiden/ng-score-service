
def health_check() -> bool:
    return True

def get_scores(size: int = None, level: int = None) -> list:
    return [
        {'name': 'player1', 'score': 14000, 'level': 0},
        {'name': 'player2', 'score': 4000, 'level': 1},
        {'name': 'player3', 'score': 84000, 'level': 0}
    ]

def get_position(score: int, level: int) -> dict:
    return {
        'position': 3
    }

def save_score(score: int, level: int, name: str) -> dict:
    return {
        'position': 30
    }
