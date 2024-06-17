import sqlalchemy as sa
from datetime import datetime, timezone
from flask import flash, render_template, redirect, request, url_for
from app import db
from app.main import bp
from app.main.forms import TodoForm
from app.models import Todo


@bp.route("/", methods=["GET"])
@bp.route("/index", methods=["GET"])
def index():
    todos = db.session.query(Todo).order_by(sa.text("id desc"))
    return render_template("index.html", todos=todos, title="Todo")


@bp.route("/<int:id>", methods=["GET"])
def detail(id):
    todo = Todo.query.filter(Todo.id == id).first()
    return render_template("detail.html", todo=todo)


@bp.route("/create", methods=["GET", "POST"])
def create():
    form = TodoForm()
    if form.validate_on_submit():
        todo = Todo(
            title=form.data.get("title"),
            content=form.data.get("content"),
            priority=form.data.get("priority"),
            deadline=form.data.get("deadline"),
            completed=form.data.get("completed"),
            created_at=datetime.now(timezone.utc),
        )
        db.session.add(todo)
        db.session.commit()
        return redirect(url_for("main.detail", id=todo.id))
    return render_template("create.html", form=form, title="할 일 등록")


@bp.route("/<int:id>/delete", methods=["POST"])
def delete(id):
    todo = Todo.query.get(id)
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("main.index"))


@bp.route("/<int:id>/update", methods=["GET", "POST"])
def update(id):
    todo = Todo.query.get(id)
    form = TodoForm(
        title=todo.title,
        content=todo.content,
        priority=todo.priority,
        deadline=todo.deadline,
        completed=todo.completed,
    )
    if request.method == "POST" and form.validate_on_submit():
        todo.title = form.data.get("title")
        todo.content = form.data.get("content")
        todo.priority = form.data.get("priority")
        todo.deadline = form.data.get("deadline")
        todo.completed = form.data.get("completed")
        db.session.commit()
        return redirect(url_for("main.detail", id=todo.id))
    return render_template("update.html", title="할 일 수정", form=form)


@bp.route("/<int:id>/toggle", methods=["GET"])
def toggle(id):
    todo = Todo.query.get(id)
    todo.completed = not todo.completed
    db.session.commit()
    return redirect(url_for("main.detail", id=todo.id))
