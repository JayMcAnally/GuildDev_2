from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from guild_dev.config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

# db = SQLAlchemy()
#
#
# def create_app(config_class=Config):
#     app = Flask(__name__)
#     app.config.from_object(Config)
#     db.init_app(app)
#     print()
#
#     return app
