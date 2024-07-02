import sqlalchemy as sa
import sqlalchemy.orm as so
from app import db


class Album(db.Model):
    id: so.Mapped[int] = db.Column(sa.Integer, primary_key=True)
    content: so.Mapped[str] = db.Column(sa.String(20))
    image: so.Mapped[str] = db.Column(sa.String)
