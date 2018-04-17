from flask import Blueprint, render_template, request
#from server.dp import data_processing
from flask_login import login_required, current_user
from server.api.recipe.model import Ingredient
from server.dp import find_matching_recipes
from server.api.recipe.img_url import fetch_img_url

recipe_blueprint = Blueprint('recipe', __name__, template_folder='./templates')


data = [{	"name": "Blue Berry Yogurt",
			"image": "https://images.unsplash.com/photo-1482423064560-3e394ae8f216?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=5f129e30860e5f930955ac0591bd57c8&auto=format&fit=crop&w=2250&q=80",
			"description": "You Have all the ingredients to make this.",
			"num_ingredients": "5",
			"id": "1234"
		},
		{	"name": "Ham and Egg Sandwich",
			"image": "https://images.unsplash.com/photo-1479894720049-067d8b87f2d9?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=ea23bfdafc40b5d5edcbb22c826ad444&auto=format&fit=crop&w=800&q=60",
			"description": "You Have all the ingredients to make this.",
			"num_ingredients": "5",
			"id": "2345"
		}
		]

@login_required
@recipe_blueprint.route('/recipe/<id>', methods=['GET'])
def detail_recipe(id=None):
    return render_template('detail_recipe.html', data=recipe)


@login_required
@recipe_blueprint.route('/recipe', methods=['GET'])
def recipe():

    ingredients_list = [ing.name for ing in current_user.get_ingridients()]
    result, result_details = find_matching_recipes(ingredients_list)

    # Adding img url to the dictionary
    for key, value in result.items():
        print(str(value))
        recipe_img_url = fetch_img_url(value['title'])
        result[key]['image'] = recipe_img_url

    return render_template('recipe.html', data=data, recipes=result)


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
