from sqlalchemy import String, Integer
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy import select
from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field


engine = create_engine("sqlite://", echo=True)


class Base(DeclarativeBase):
    pass


class Scores(Base):
    __tablename__ = "scores"
    id: Mapped[str] = mapped_column(primary_key=True)
    user_name: Mapped[str] = mapped_column(String(30))
    score: Mapped[int] = mapped_column(Integer)
    level: Mapped[int] = mapped_column(Integer)

    def __repr__(self) -> str:
        return f"id:{self.id!r}, user_name:{self.user_name!r}, score:{self.score!r}, level:{self.level!r}"


class ScoresSchema(SQLAlchemySchema):
    class Meta:
        model = Scores
        load_instance = True

    id = auto_field()
    user_name = auto_field()
    score = auto_field()
    level = auto_field()


def create_all():
    Base.metadata.create_all(engine)


def insert_data(id: str, score: int, level: int, user_name: str) -> int:
    with Session(engine) as session:

        new_score = Scores(
            id=id,
            score=score,
            level=level,
            user_name=user_name
        )

        session.add(new_score)
        session.commit()


def get_data(chunk_size: int, level: int) -> dict:
    scores_schema = ScoresSchema(many=True)

    with Session(engine) as session:
        statement = select(Scores).where(Scores.level == level).order_by(Scores.score.desc()).limit(chunk_size)
        result = session.scalars(statement).all()
        return scores_schema.dump(result)


create_all()
insert_data('3ef42114-a2c6-41e4-960b-1256c54c0800', '1000', 1, 'Player1')
insert_data('3ef42114-a2c6-41e4-960b-1256c54c0801', '14011', 1, 'Player2')
insert_data('3ef42114-a2c6-41e4-960b-1256c54c0802', '12022', 1, 'Player3')
insert_data('3ef42114-a2c6-41e4-960b-1256c54c0803', '11003', 0, 'Player4')
insert_data('3ef42114-a2c6-41e4-960b-1256c54c0804', '17004', 1, 'Player5')
insert_data('3ef42114-a2c6-41e4-960b-1256c54c0805', '12015', 1, 'Player6')
insert_data('3ef42114-a2c6-41e4-960b-1256c54c0806', '12006', 0, 'Player7')
insert_data('3ef42114-a2c6-41e4-960b-1256c54c0807', '10000', 2, 'Player8')
insert_data('3ef42114-a2c6-41e4-960b-1256c54c0808', '12018', 2, 'Player9')
