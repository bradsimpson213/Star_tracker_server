from flask import Flask, render_template # NOQA
from .config import Config
from .models import db
from .routes import users
from flask_migrate import Migrate


app = Flask(__name__)
app.config.from_object(Config)

app.register_blueprint(users.bp)
# app.register_blueprint(ships.bp)

db.init_app(app)
migrate = Migrate(app, db)



# @app.route("/")
# def home():
#     return render_template("main_page.html")
