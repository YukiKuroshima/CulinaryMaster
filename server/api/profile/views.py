from flask import Blueprint, render_template, redirect
from flask_login import login_required, current_user
from server.api.profile.form import EditProfileForm
import json

profile_blueprint = Blueprint('profile', __name__, template_folder='./templates')




@profile_blueprint.route('/profile', methods=['GET'])
@login_required
def profile():
    return render_template('profile.html', data=current_user)

@profile_blueprint.route('/profile/edit', methods=['GET', 'POST'])
@login_required
def edit_profile():
	form = EditProfileForm()
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
			#put updated name and image to database
			current_user.update_name(first_name, last_name)
			current_user.update_image(image)
			return redirect("/profile")
	return render_template('edit.html', form=form)
