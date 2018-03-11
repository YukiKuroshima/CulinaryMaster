from flask import Blueprint, render_template
from flask_login import login_required
from server.api.profile.form import EditProfileForm

profile_blueprint = Blueprint('profile', __name__, template_folder='./templates')


@profile_blueprint.route('/profile', methods=['GET'])
@login_required
def profile():
    return render_template('profile.html')

@profile_blueprint.route('/profile/edit', methods=['GET', 'POST'])
@login_required
def edit_profile():
	form = EditProfileForm()
	if form.validate_on_submit():
		name = form.name.data
		image = form.imageURL.data
		data = {name: name, image: image}
		if name is None:
			form.name.errors.append('Invalid Name')
		elif image is None:
			form.image.errors.append('Invalid image url')
		else:
			return redirect("/profile", data)
	return render_template('edit.html', form=form)