import sqlalchemy as sa
from flask import flash, redirect, render_template, url_for
from flask_login import login_user, logout_user, current_user
from app import db
from app.auth import bp
from app.auth.forms import LoginForm, RegistrationForm
from app.models import Account


@bp.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("reviews.index"))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = Account(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("가입이 완료되었습니다.")
        return redirect(url_for("reviews.index"))
    return render_template("auth/register.html", title="회원가입", form=form)


@bp.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("reviews.index"))
    form = LoginForm()
    if form.validate_on_submit():
        user = db.session.scalar(
            sa.select(Account).where(Account.username == form.username.data)
        )
        if user is None or not user.check_password(form.password.data):
            flash("잘못된 아이디 또는 비밀번호입니다.")
            return redirect(url_for("auth.login"))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for("reviews.index"))
    return render_template("auth/login.html", title="로그인", form=form)


@bp.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("reviews.index"))
