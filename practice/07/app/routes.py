import sqlalchemy as sa
from datetime import datetime, timezone
from flask import render_template, request
from app import app, db
from app.forms import TodoForm
from app.models import Todo


@app.route("/")
@app.route("/index")
def index():
    todos = db.session.query(Todo).order_by(sa.text("id desc"))
    return render_template("index.html", todos=todos, title="Todo")


@app.route("/<todo_id>")
def detail(todo_id):
    todo = db.session.get(Todo, todo_id)
    return render_template("detail.html", todo=todo, title=todo.title)


@app.route("/create", methods=["GET", "POST"])
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
        return render_template("create.html", title="등록 완료")
    return render_template("new.html", form=form, title="할 일 등록")
