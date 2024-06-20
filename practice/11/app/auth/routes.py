from flask import redirect, url_for, render_template
from flask_login import current_user, login_user, login_required, logout_user
from app import db
from app.auth import bp
from app.auth.forms import LoginForm, RegistrationForm, UserUpdateForm, PasswordForm
from app.models import User


@bp.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter(User.username == form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            return redirect(url_for("auth.login"))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for("main.index"))
    return render_template("auth/login.html", form=form, title="로그인")


@bp.route("/logout", methods=["GET"])
def logout():
    logout_user()
    return redirect(url_for("main.index"))


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
        return redirect(url_for("auth.login"))
    return render_template("auth/register.html", form=form, title="회원가입")


@login_required
@bp.route("/delete", methods=["POST"])
def delete():
    db.session.delete(current_user)
    db.session.commit()
    logout_user()
    return redirect(url_for("main.index"))


@login_required
@bp.route("/update", methods=["GET", "POST"])
def update():
    form = UserUpdateForm(
        username=current_user.username,
        email=current_user.email
    )
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        return redirect(url_for("main.index"))
    return render_template("auth/update.html", form=form, title="회원 정보 수정")


@login_required
@bp.route("/password", methods=["GET", "POST"])
def password():
    form = PasswordForm()
    if form.validate_on_submit():
        current_user.set_password(form.password.data)
        db.session.commit()
        return redirect(url_for("main.index"))
    return render_template("auth/password.html", form=form, title="비밀번호 수정")
