from sqlalchemy import String, Integer
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy import select


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

    stmt = select(Scores)

    # for user in session.scalars(stmt):
    #     print(user)
    return [x for x in session.scalars(stmt)]



create_all()
# insert_data('abc123', 3000, 1, 'Player1')
# get_data()
