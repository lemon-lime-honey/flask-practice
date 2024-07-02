from flask_wtf import FlaskForm
from wtforms import StringField, FileField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError
from app import app


def allowed_file(filename):
    return (
        "." in filename
        and filename.rsplit(".", 1)[1].lower() in app.config["ALLOWED_EXTENSIONS"]
    )


class AlbumForm(FlaskForm):
    content = StringField("내용", validators=[Length(max=20)])
    image = FileField("사진", validators=[DataRequired()])
    submit = SubmitField("등록")

    def validate_image(self, image):
        if (
            not image.data
            or not image.data.filename
            or not allowed_file(image.data.filename)
        ):
            raise ValidationError("이미지를 선택하세요.")
