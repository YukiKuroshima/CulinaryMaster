from flask import Blueprint, render_template, request
#from server.dp import data_processing
from flask_login import  login_required, current_user
from server.api.recipe.model import Ingredient

recipe_blueprint = Blueprint('recipe', __name__, template_folder='./templates')


@login_required
@recipe_blueprint.route('/recipe', methods=['GET'])
def recipe():

    #data = data_processing()
    return render_template('recipe.html', data=data)


@login_required
@recipe_blueprint.route('/newInventory', methods=['GET'])
def newInventory():
    ingridients = current_user.get_ingridients()
    return render_template('newInventory.html', ingridients=ingridients)


@login_required
@recipe_blueprint.route('/ingridient', methods=['POST'])
def add_ingridient():
    current_user.add_ingridient(request.form['item'])
    return render_template('newInventory.html')


@login_required
@recipe_blueprint.route('/ingridient', methods=['DELETE'])
def delete_ingridient():
    current_user.remove_ingridient(request.form['item'])
    return render_template('newInventory.html')
