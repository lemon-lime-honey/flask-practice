from datetime import date
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DateField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length


class TodoForm(FlaskForm):
    title = StringField("제목", validators=[DataRequired(), Length(min=1, max=80)])
    content = TextAreaField("내용")
    priority = IntegerField("우선순위", default=3)
    deadline = DateField("마감기한", default=date.today)
    completed = BooleanField("완료여부", default=False)
    submit = SubmitField("등록")
