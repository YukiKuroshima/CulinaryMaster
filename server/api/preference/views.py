from flask import Blueprint, render_template, redirect
from flask_login import login_required, current_user
from server.api.preference.form import EditPreferenceForm
import json

preference_blueprint = Blueprint('preference', __name__, template_folder='./templates')


@preference_blueprint.route('/preference', methods=['GET', 'POST'])
@login_required
def profile():
    form = EditPreferenceForm()
    if form.validate_on_submit():
        first_name = form.first_name.data
        last_name = form.last_name.data
        image = form.imageURL.data
        if first_name is None:
            form.first_name.errors.append('Invalid first name')
        elif last_name is None:
            form.last_name.errors.append('Invalid last name')
        elif image is None:
            form.image.errors.append('Invalid image url')
        else:
            current_user.update_name(first_name, last_name)
            current_user.update_image(image)
            return redirect("/preference")
    return render_template('preference.html', data=current_user, form=form)
