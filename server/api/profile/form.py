from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Length


class EditProfileForm(FlaskForm):
    name = StringField(
            'name',
            validators=[
                InputRequired(message='Name is required'),
                Length(min=8, max=30),
                ],
            render_kw={"placeholder": "Name"}
            )
    imageURL = StringField(
            'image',
            validators=[
                InputRequired(message='imageUrl is required'),
                
                ],
            render_kw={"placeholder": "image url"}
            )
