from flask import Blueprint, render_template

recipe_blueprint = Blueprint('recipe', __name__, template_folder='./templates')


@recipe_blueprint.route('/recipe', methods=['GET'])
def recipe():
    return render_template('recipe.html')
