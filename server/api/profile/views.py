from flask import Blueprint, render_template, redirect
from flask_login import login_required
from server.api.profile.form import EditProfileForm
import json

profile_blueprint = Blueprint('profile', __name__, template_folder='./templates')

data = {}
data['name'] = 'Duoc Nguyen'
data['image'] = 'http://www.personalbrandingblog.com/wp-content/uploads/2017/08/blank-profile-picture-973460_640-300x300.png'
json_data = json.dumps(data)

@profile_blueprint.route('/profile', methods=['GET'])
@login_required
def profile():
    return render_template('profile.html', data=data)

@profile_blueprint.route('/profile/edit', methods=['GET', 'POST'])
@login_required
def edit_profile():
	form = EditProfileForm()
	if form.validate_on_submit():
		name = form.name.data
		image = form.imageURL.data
		if name is None:
			form.name.errors.append('Invalid Name')
		elif image is None:
			form.image.errors.append('Invalid image url')
		else:
			data[]
			return redirect("/profile")
	return render_template('edit.html', form=form)