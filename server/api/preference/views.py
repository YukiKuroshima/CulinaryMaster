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
        allergy_str = form.allergy.data
        allergy_list = [x.strip() for x in allergy_str.split(',')]
        current_user.remove_all_allergies()
        current_user.add_allergies(allergy_list)
        #Change class allergy to preference
        #change allergy table to preference table
        #have column for allergy, 
        #have column for diet pref 
        return redirect("/preference")

    else:
        allergies = current_user.get_allergies()
        print(allergies)
        return render_template('preference.html', allergies=allergies, form=form)
