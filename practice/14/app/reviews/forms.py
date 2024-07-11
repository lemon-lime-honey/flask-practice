from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length


class ReviewForm(FlaskForm):
    title = StringField("제목", validators=[DataRequired(), Length(min=1, max=20)])
    book = StringField("책 제목")
    content = TextAreaField("내용", validators=[DataRequired()])
    submit = SubmitField("등록")


class CommentForm(FlaskForm):
    content = StringField(validators=[DataRequired()])
    submit = SubmitField("등록")
