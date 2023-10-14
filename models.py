from sqlalchemy import Integer, String, Float
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped
from flask_sqlalchemy import SQLAlchemy


class Base(DeclarativeBase):
    pass


# creating sqlite obj
db = SQLAlchemy(model_class=Base)


# creating the db model
class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), nullable=False, unique=True)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)
