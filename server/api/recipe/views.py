from flask import Blueprint, render_template
from server.dp import data_processing

recipe_blueprint = Blueprint('recipe', __name__, template_folder='./templates')


@recipe_blueprint.route('/recipe', methods=['GET'])
def recipe():

    data = data_processing()
    return render_template('recipe.html', data=data)

@recipe_blueprint.route('/newInventory', methods=['GET'])
def newInventory():

    return render_template('newInventory.html')




