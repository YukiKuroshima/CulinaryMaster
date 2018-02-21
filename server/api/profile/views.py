from flask import Blueprint, render_template

profile_blueprint = Blueprint('profile', __name__, template_folder='./templates')


@profile_blueprint.route('/profile', methods=['GET'])
def profile():
    return render_template('profile.html')
