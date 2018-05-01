from flask import Blueprint, render_template, request
#from server.dp import data_processing
from flask_login import login_required, current_user
from server.api.recipe.model import Ingredient
from server.dp import find_matching_recipes, find_recipe_by_id
from server.api.recipe.img_url import fetch_img_url

recipe_blueprint = Blueprint('recipe', __name__, template_folder='./templates')


@login_required
@recipe_blueprint.route('/recipe/<id>', methods=['GET'])
def detail_recipe(id=None):
    print("Recipe id: " + id)
    recipe = find_recipe_by_id(id)
    recipe_img_url = fetch_img_url(recipe['title'])
    return render_template('detail_recipe.html', recipe=recipe, image=recipe_img_url)


@login_required
@recipe_blueprint.route('/recipe', methods=['GET'])
def recipe():

    ingredients_list = [ing.name for ing in current_user.get_ingridients()]
    result, result_details = find_matching_recipes(ingredients_list)

    # Adding img url to the dictionary
    for key, value in result.items():
        #print(str(value))
        recipe_img_url = fetch_img_url(value['title'])
        result[key]['image'] = recipe_img_url

    return render_template('recipe.html', recipes=result)


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
