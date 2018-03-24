from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import InputRequired, Length


class EditPreferenceForm(FlaskForm):
    first_name = StringField(
            'first_name',
            validators=[
                InputRequired(message='First name is required'),
                Length(min=1, max=30),
                ],
            render_kw={"placeholder": "First Name"}
            )
    last_name = StringField(
            'last_name',
            validators=[
                InputRequired(message='Last name is required'),
                Length(min=1, max=30),
                ],
            render_kw={"placeholder": "Last Name"}
            )
    imageURL = StringField(
            'image',
            validators=[
                InputRequired(message='imageUrl is required'),
                
                ],
            render_kw={"placeholder": "image url"}
            )
