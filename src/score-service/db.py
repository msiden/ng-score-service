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


# Create database
def create_all():
    Base.metadata.create_all(engine)


# Write data to DB
def insert_data():
    with Session(engine) as session:
        spongebob = Scores(
            id="1",
            user_name="spongebob",
            score=1000,
            level=0
        )
        sandy = Scores(
            id="2",
            user_name="sandy",
            score=1200,
            level=0
        )

        session.add_all([spongebob, sandy])
        session.commit()


def get_data():
    session = Session(engine)

    stmt = select(Scores).where(Scores.user_name.in_(["spongebob", "sandy"]))

    for user in session.scalars(stmt):
        print(user)


if __name__ == "__main__":
    create_all()
    insert_data()
    get_data()

