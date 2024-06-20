import sqlalchemy as sa
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo
from app import db
from app.models import User


class RegistrationForm(FlaskForm):
    username = StringField("아이디", validators=[DataRequired()])
    email = StringField("이메일", validators=[DataRequired(), Email()])
    password = PasswordField("비밀번호", validators=[DataRequired()])
    password2 = PasswordField(
        "비밀번호 반복", validators=[DataRequired(), EqualTo("password")]
    )
    submit = SubmitField("가입")

    def validate_username(self, username):
        user = db.session.scalar(sa.select(User).where(User.username == username.data))

        if user is not None:
            raise ValidationError("이미 존재하는 아이디입니다.")

    def validate_email(self, email):
        user = db.session.scalar(sa.select(User).where(User.email == email.data))

        if user is not None:
            raise ValidationError("다른 이메일을 사용하십시오.")


class LoginForm(FlaskForm):
    username = StringField("아이디", validators=[DataRequired()])
    password = PasswordField("비밀번호", validators=[DataRequired()])
    remember_me = BooleanField("로그인 유지")
    submit = SubmitField("로그인")


class UserUpdateForm(FlaskForm):
    username = StringField("아이디", validators=[DataRequired()])
    email = StringField("이메일", validators=[DataRequired(), Email()])
    submit = SubmitField("로그인")

    def validate_username(self, username):
        user = db.session.scalar(sa.select(User).where(User.username == username.data))

        if user is None or user.username == username.data:
            return

        raise ValidationError("이미 존재하는 아이디입니다.")

    def validate_email(self, email):
        user = db.session.scalar(sa.select(User).where(User.email == email.data))

        if user is None or user.email == email.data:
            return

        raise ValidationError("다른 이메일을 사용하십시오.")


class PasswordForm(FlaskForm):
    password = PasswordField("비밀번호", validators=[DataRequired()])
    password2 = PasswordField(
        "비밀번호 반복", validators=[DataRequired(), EqualTo("password")]
    )
    submit = SubmitField("가입")
