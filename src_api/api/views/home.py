from flask import Blueprint
from flask import current_app

home = Blueprint('home', __name__)


@home.route('/')
def index():
    return str("Measure ALIVE....")
