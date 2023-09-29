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
        load_instance = True  # Optional: deserialize to model instances
        fields = ("id", "user_name")

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


def get_data():
    session = Session(engine)

    statement = select(Scores)

    # scores = Scores(id="3ef42114-a2c6-41e4-960b-1256c54c0800")
    scores_schema = ScoresSchema(many=True)
    # session.add(scores)
    # session.commit()

    # dump_data = scores_schema.dump(scores)
    # print('>', dump_data)

    # load_data = scores_schema.load(session.execute(statement), session=session)
    # print(load_data)


    # return [score for score in session.execute(statement)]

    result = session.execute(statement)
    # print('result', result)
    # load_data = scores_schema.dump(result)
    # print('>', load_data)

    for r in result:
        load_data = scores_schema.dump(r)
        print('>>>', load_data, type(load_data), type(load_data[0]))

    # with Session(engine) as session:
    #     statement = select(Scores)
    #     return session.scalars(statement).all()

create_all()
insert_data('3ef42114-a2c6-41e4-960b-1256c54c0800', '12000', 1, 'Player1')
insert_data('3ef42114-a2c6-41e4-960b-1256c54c0801', '12001', 1, 'Player2')
insert_data('3ef42114-a2c6-41e4-960b-1256c54c0802', '12002', 1, 'Player3')
# get_data()
