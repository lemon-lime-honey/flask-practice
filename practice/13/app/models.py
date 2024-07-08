import sqlalchemy as sa
import sqlalchemy.orm as so
from datetime import datetime, timezone
from typing import Optional
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app import db, login


class Account(UserMixin, db.Model):
    id: so.Mapped[int] = so.mapped_column(sa.Integer, primary_key=True)
    username: so.Mapped[str] = so.mapped_column(sa.String(64), index=True, unique=True)
    email: so.Mapped[str] = so.mapped_column(sa.String(120), index=True, unique=True)
    password_hash: so.Mapped[Optional[str]] = so.mapped_column(sa.String(256))
    
    review: so.Mapped[list["Review"]] = so.relationship(back_populates="account")
    comment: so.Mapped[list["Comment"]] = so.relationship(back_populates="account")

    def __repr__(self):
        return f"<User {self.username}>"

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Review(db.Model):
    id: so.Mapped[int] = so.mapped_column(sa.Integer, primary_key=True)
    title: so.Mapped[str] = so.mapped_column(sa.String(20))
    content: so.Mapped[str] = so.mapped_column(sa.Text)
    book: so.Mapped[str] = so.mapped_column(sa.String(20))
    created_at: so.Mapped[datetime] = so.mapped_column(
        sa.DateTime, default=datetime.now(timezone.utc)
    )
    updated_at: so.Mapped[datetime] = so.mapped_column(
        sa.DateTime,
        default=datetime.now(timezone.utc),
        onupdate=datetime.now(timezone.utc),
    )
    account_id: so.Mapped[int] = so.mapped_column(sa.ForeignKey("account.id", ondelete="CASCADE"))
    account: so.Mapped["Account"] = so.relationship(back_populates="review")
    comment: so.Mapped[list["Comment"]] = so.relationship(back_populates="review")

    def __repr__(self):
        return f"<Review {self.title:.5} by User {self.author.username}>"


class Comment(db.Model):
    id: so.Mapped[int] = db.Column(sa.Integer, primary_key=True)
    content: so.Mapped[str] = db.Column(sa.String(300))
    created_at: so.Mapped[datetime] = db.Column(
        sa.DateTime, default=datetime.now(timezone.utc)
    )
    updated_at: so.Mapped[datetime] = db.Column(
        sa.DateTime,
        default=datetime.now(timezone.utc),
        onupdate=datetime.now(timezone.utc),
    )
    account_id: so.Mapped[int] = so.mapped_column(sa.ForeignKey("account.id", ondelete="CASCADE"), nullable=False)
    account: so.Mapped["Account"] = so.relationship(back_populates="comment")
    review_id: so.Mapped[int] = so.mapped_column(sa.ForeignKey("review.id", ondelete="CASCADE"), nullable=False)
    review: so.Mapped["Review"] = so.relationship(back_populates="comment")

    def __repr__(self):
        return f"<Comment {self.content:.5} by User {self.author.username}>"


@login.user_loader
def load_user(id):
    return db.session.get(Account, int(id))
