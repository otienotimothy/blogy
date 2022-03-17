from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, BooleanField, TextAreaField, SubmitField
from wtforms.validators import Email, InputRequired, Length, EqualTo

class SubscribeForm(FlaskForm):
    email = EmailField('Email', validators=[InputRequired(), Email()], render_kw={'placeholder': 'Enter your Email'})
    submit = SubmitField('Subscribe')

class CreateUserForm(FlaskForm):
    email = EmailField('What\'s your Email?', validators=[InputRequired(), Email()])
    username = StringField('Add your prefered Username', validators=[InputRequired(), Length(max=15)])
    password = PasswordField('Enter a Password', validators=[InputRequired(), Length(min=8)])
    confirm_password = PasswordField('Confirm Password', validators=[InputRequired(), Length(min=8), EqualTo('password')])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email = EmailField('What\'s your Email?', validators=[
                       InputRequired(), Email()])

    password = PasswordField('Enter a Password', validators=[
                             InputRequired(), Length(min=8)])

    remember_me = BooleanField('Remember Me')

    submit = SubmitField('Login')

class CommentForm(FlaskForm):
    text = StringField('Comment', validators=[InputRequired(), Length(max=200)])

    submit = SubmitField('Comment')

class BlogForm(FlaskForm):
    title = StringField('Title', validators=[InputRequired(), Length(120)])

    text = TextAreaField('Blog Content', validators=[InputRequired()], render_kw={'rows':4})

    submit = SubmitField('Create Blog')