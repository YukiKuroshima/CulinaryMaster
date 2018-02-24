from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Email, Length


class SignupForm(FlaskForm):
    first_name = StringField(
            'First Name',
            validators=[
                InputRequired(message='First name is required'),
                Length(min=1),
                ],
            render_kw={"placeholder": "First Name"}
            )
    last_name = StringField(
            'Last Name',
            validators=[
                InputRequired(message='Last name is required'),
                Length(min=1),
                ],
            render_kw={"placeholder": "Last Name"}
            )
    email = StringField(
            'Email',
            validators=[
                InputRequired(message='Email is required'),
                Email()
                ],
            render_kw={"placeholder": "example@gmail.com"}
            )
    password = PasswordField(
            'Password',
            validators=[
                InputRequired('Password is required'),
                Length(min=8, max=30),
                ],
            render_kw={"placeholder": "Password"}
            )


class LoginForm(FlaskForm):
    email = StringField(
            'Email',
            validators=[
                InputRequired(message='Email is required'),
                Email()
                ],
            render_kw={"placeholder": "example@gmail.com"}
            )
    password = PasswordField(
            'Password',
            validators=[
                InputRequired('Password is required'),
                Length(min=8, max=30),
                ],
            render_kw={"placeholder": "Password"}
            )
