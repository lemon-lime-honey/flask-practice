import sqlalchemy as sa
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from app import db
from app.models import Account


class RegistrationForm(FlaskForm):
    username = StringField("아이디", validators=[DataRequired()])
    email = StringField("이메일", validators=[DataRequired(), Email()])
    password = PasswordField("비밀번호", validators=[DataRequired()])
    password2 = PasswordField(
        "비밀번호 반복", validators=[DataRequired(), EqualTo("password")]
    )
    submit = SubmitField("가입")

    def validate_username(self, username):
        user = db.session.scalar(sa.select(Account).where(Account.username == username.data))
        if user is not None:
            raise ValidationError("다른 아이디를 입력하세요.")

    def validate_email(self, email):
        user = db.session.scalar(sa.select(Account).where(Account.email == email.data))
        if user is not None:
            raise ValidationError("다른 이메일 주소를 입력하세요.")


class LoginForm(FlaskForm):
    username = StringField("아이디", validators=[DataRequired()])
    password = PasswordField("비밀번호", validators=[DataRequired()])
    remember_me = BooleanField("로그인 유지")
    submit = SubmitField("로그인")
