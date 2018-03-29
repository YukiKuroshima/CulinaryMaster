from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from wtforms.validators import InputRequired, Length


class EditPreferenceForm(FlaskForm):
    allergy = StringField(
            'allergy',
            validators=[
                InputRequired(message='Please input your allergy'),
                Length(min=1, max=50),
                ],
            render_kw={"placeholder": "Please input your allergy (separate by comma)"}
            )
    diet_pref = SelectField(
    		'diet_pref', 
    		choices = [('healthy', 'Stay Healthy'), 
    		('lose', 'Lose Weight'), 
    		('gain', 'Gain Weight')]
    		)
