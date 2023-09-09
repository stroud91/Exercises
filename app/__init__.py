from flask import (Flask, render_template)
# import config class
from app.config import Config
# import form class
from app import routes


app = Flask(__name__)
# populate Flask config dictionary from config class
app.config.from_object(Config)

app.register_blueprint(routes.inventory.bp)
app.register_blueprint(routes.main.bp)
