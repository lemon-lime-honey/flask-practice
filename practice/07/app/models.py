import sqlalchemy as sa
import sqlalchemy.orm as so
from datetime import date, datetime, timezone
from typing import Optional
from app import db


class Todo(db.Model):
    __tablename__ = "todo"

    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    title: so.Mapped[str] = so.mapped_column(sa.String(80), nullable=False)
    content: so.Mapped[Optional[str]] = so.mapped_column(sa.String(), nullable=True)
    completed: so.Mapped[bool] = so.mapped_column(sa.Boolean)
    priority: so.Mapped[int] = so.mapped_column(sa.Integer, default=3)
    created_at: so.Mapped[datetime] = so.mapped_column(index=True, default=lambda: datetime.now(timezone.utc))
    deadline: so.Mapped[date] = so.mapped_column(sa.Date)
