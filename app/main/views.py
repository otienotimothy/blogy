from flask import Blueprint, render_template
from app.forms import SubscribeForm

views = Blueprint('views', __name__)

@views.route('/')
def index():
    subscribe = SubscribeForm()
    return render_template('index.html', subscribe = subscribe)