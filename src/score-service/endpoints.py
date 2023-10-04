import db


def health_check() -> dict:
    return {
        'status': 'ok'
    }


def get_scores(chunk_size: int = None, level: int = None) -> list:
    return db.get_data(chunk_size, level)


def save_score(game_id: str, score: int, level: int, user_name: str) -> None:
    db.insert_data(game_id, score, level, user_name)
