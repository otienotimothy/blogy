from flask_wtf import FlaskForm
from wtforms import EmailField, SubmitField
from wtforms.validators import Email, InputRequired

class SubscribeForm(FlaskForm):
    email = EmailField('Email', validators=[InputRequired(), Email()], render_kw={'placeholder': 'Enter your Email'})
    submit = SubmitField('Subscribe')