import sqlalchemy as sa
from flask import flash, render_template, redirect, url_for
from flask_login import current_user, login_user, logout_user
from app import db
from app.auth import bp
from app.auth.forms import RegistrationForm, LoginForm
from app.models import User


@bp.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("main.index"))

    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("가입이 완료되었습니다.")
        return redirect(url_for("auth.login"))
    return render_template("auth/register.html", form=form, title="회원가입")


@bp.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("main.index"))

    form = LoginForm()
    if form.validate_on_submit():
        user = db.session.scalar(
            sa.select(User).where(User.username == form.username.data)
        )
        if user is None or not user.check_password(form.password.data):
            flash("아이디 또는 비밀번호를 다시 확인하세요.")
            return redirect(url_for("auth.login"))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for("main.index"))
    return render_template("auth/login.html", form=form, title="로그인")


@bp.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("main.index"))
