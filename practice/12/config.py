import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, ".env"))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL"
    ) or "sqlite:///db.sqlite3"
    UPLOAD_FOLDER = os.path.join('static', 'image')
    ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png', 'gif'}
