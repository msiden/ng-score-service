import pytest
import db

def test_connect_with_engine(self):
    db.create_all()
    db.insert_data('abc123', 3000, 1, 'Player1')
    db.get_data()
