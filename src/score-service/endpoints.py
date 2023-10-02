import db


def health_check() -> dict:
    return {
        'status': 'ok'
    }

def get_scores(chunk_size: int = None, level: int = None) -> list:
    return db.get_data(chunk_size, level)


def get_position(score: int, level: int) -> dict:
    return {
        'position': 3
    }


def save_score(game_id: str, score: int, level: int, user_name: str) -> dict:
    db.insert_data(game_id, score, level, user_name)
    return {
        'position': 30
    }
