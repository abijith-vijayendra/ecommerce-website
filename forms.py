from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class SignupForm(FlaskForm):
    first_name = StringField("First_name", validators = [DataRequired("Please enter your first name")])
    last_name = StringField("Last name", validators = [DataRequired("Please enter your last name")])
    email = StringField("Email", validators = [DataRequired("Please enter a valid email"), Email("Please enter a valid email address")])
    password = PasswordField("Password", validators = [DataRequired("Please enter the password"), Length(min =6, message = "Length must be greater than 6 characters")])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email = StringField("Email", validators = [DataRequired("Please enter your registered email address"), Email("Please enter a valid Email ID")])
    password = PasswordField("Password", validators = [DataRequired("Password Required")])
    submit = SubmitField("Sign In")

class SearchForm(FlaskForm):
    search = StringField("Search", validators = [DataRequired("Please enter the product you are looking for")])
    submit = SubmitField("Search")
