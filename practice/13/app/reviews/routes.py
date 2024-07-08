import sqlalchemy as sa
from flask import flash, redirect, render_template, url_for
from flask_login import current_user
from app import db
from app.models import Comment, Review
from app.reviews import bp
from app.reviews.forms import ReviewForm, CommentForm


@bp.route("/", methods=["GET", "POST"])
@bp.route("/index", methods=["GET", "POST"])
def index():
    form = ReviewForm()
    if current_user.is_authenticated and form.validate_on_submit():
        review = Review(
            title=form.title.data,
            content=form.content.data,
            book=form.book.data,
            account=current_user,
        )
        db.session.add(review)
        db.session.commit()
        flash("후기가 등록되었습니다.")
        return redirect(url_for("reviews.index"))
    reviews = db.session.scalars(sa.select(Review))
    return render_template("index.html", title="책 후기", form=form, reviews=reviews)


@bp.route("/<int:id>", methods=["GET", "POST"])
def detail(id):
    review = db.session.scalar(sa.select(Review).where(Review.id == id))
    comments = db.session.scalars(sa.select(Comment).where(Comment.review_id == id)).all()
    form = ReviewForm()
    commentform = CommentForm()
    if commentform.validate_on_submit():
        comment = Comment(
            content=commentform.content.data, account=current_user,
            review=review
        )
        db.session.add(comment)
        db.session.commit()
        flash("댓글이 등록되었습니다.")
        return redirect(url_for("reviews.detail", id=id))
    return render_template(
        "detail.html",
        review=review,
        comments=comments,
        form=form,
        commentform=commentform,
    )
