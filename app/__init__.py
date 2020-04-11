from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
from flask_wtf.csrf import CSRFProtect

import os

basedir = os.path.abspath(os.path.dirname(__file__))

csrf = CSRFProtect()
app = Flask(__name__)
bootstrap = Bootstrap(app)
csrf.init_app(app)

CKEDITOR_ENABLE_CSRF = True
WTF_CSRF_ENABLED = False
WTF_CSRF_SECRET_KEY = 'a random string'

app.config['SECRET_KEY'] = 'super_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL") or "sqlite:///" + os.path.join(basedir, "app.db")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes
