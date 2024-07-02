import os
import sqlalchemy as sa
from flask import flash, redirect, render_template, request, url_for
from werkzeug.utils import secure_filename
from app import app, db
from app.forms import AlbumForm
from app.models import Album


@app.route("/", methods=["GET", "POST"])
@app.route("/index", methods=["GET", "POST"])
def index():
    form = AlbumForm()
    if form.validate_on_submit():
        image = request.files["image"]
        name = secure_filename(image.filename)
        image.save(os.path.join(app.config["UPLOAD_FOLDER"], name))
        album = Album(content=form.content.data, image='image/'+name)
        db.session.add(album)
        db.session.commit()
        return redirect(url_for("index"))
    albums = db.session.query(Album).order_by(sa.text("Album.id desc"))
    return render_template("index.html", form=form, albums=albums)
